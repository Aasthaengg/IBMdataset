from collections import deque

n, k = map(int, input().split())

MOD = 1000000007

g = [[] * 1 for i in range(n)]

for i in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

d = [-1 for i in range(n)]

q = deque([])
num = k-1
d[0] = k
for to in g[0]:
    if d[to] == -1:
        d[to] = num
        num -= 1
        if num < 0:
            num = 0
        q.append(to)

while q:
    v = q.popleft()
    num = k-2
    for to in g[v]:
        if d[to] == -1:
            d[to] = num
            num -= 1
            if num < 0:
                num = 0
            q.append(to)

ans = 1
for i in d:
    ans *= i
    ans %= MOD

print(ans)