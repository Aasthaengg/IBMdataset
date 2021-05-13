from collections import defaultdict, deque

n, k = map(int, input().split())
a = tuple(map(int, input().split()))
acc = [0]
t = 0
for a_ in a:
    t = (t + a_ - 1) % k
    acc.append(t)

d = defaultdict(int)

ret = 0
count = 0
dq = deque()

for acc_ in acc:
    ret += d[acc_]
    d[acc_] += 1
    dq.append(acc_)
    if len(dq) >= k:
        v = dq.popleft()
        d[v] -= 1
print(ret)
