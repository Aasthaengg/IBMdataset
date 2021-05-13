from sys import setrecursionlimit
setrecursionlimit(10 ** 7)

n, m = map(int, input().split())

dp = [-1 for _ in range(n)]
V = [[] for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    V[x-1].append(y-1)

def f(x):
    if dp[x] != -1:
        return dp[x]

    t = 0
    for v in V[x]:
        t = max(t, f(v)+1)

    dp[x] = t
    return dp[x]

t = 0
for i in range(n):
    t = max(t, f(i))

print(t)
