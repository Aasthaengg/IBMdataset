from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
h = list(map(int, input().split()))
eg = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    eg[a - 1].append(b - 1)
    eg[b - 1].append(a - 1)

ans = 0
for i in range(n):
    high = True
    for to in eg[i]:
        if h[i] <= h[to]:
            high = False
    if high:
        ans += 1
print(ans)
