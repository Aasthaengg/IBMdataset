from collections import deque
N, K = map(int, input().split())
dt = []
for _ in range(N):
    t, d = map(int, input().split())
    dt.append((d, t))
dt.sort(reverse=True)

s = set()
bests = []
rems = deque()
for d, t in dt:
    if t in s:
        rems.append(d)
    else:
        s.add(t)
        bests.append(d)
    if len(bests) == K:
        break
x = len(bests)
k = x
p = sum(bests) + x * x
while k < K:
    p += rems.popleft()
    k += 1
maxp = p
while len(rems) and rems[0] > bests[-1]:
    p -= bests.pop() + x * x
    x -= 1
    p += rems.popleft() + x * x
    maxp = max(maxp, p)
print(maxp)
