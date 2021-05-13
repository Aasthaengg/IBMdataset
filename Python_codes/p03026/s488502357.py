from collections import deque

N = int(input())
link = [[] * N for _ in range(N)]

for i in range(N-1):
    a, b = map(lambda x: int(x) - 1, input().split())
    link[a].append(b)
    link[b].append(a)

c = list(map(int, input().split()))
c = sorted(c, reverse=True)
sums = sum(c) - max(c)

q = deque([0])
d = [-1] * N

num = 0
while len(q) > 0:
    x = q.popleft()
    d[x] = c[num]
    num += 1
    for y in link[x]:
        if d[y] < 0:
            q.append(y)

print(sums)
print(*d)