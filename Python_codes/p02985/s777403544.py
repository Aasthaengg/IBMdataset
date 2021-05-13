MOD = 10 ** 9 + 7
n, k = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
s = [0]
d = [-1] * n
while s:
    p = s.pop()
    if d[p] == -1:
        s.append(p)
        d[p] = -2
        for node in g[p]:
            if d[node] == -1:
                s.append(node)
    else:
        res = 1
        if s:
            t = k - 2
        else:
            t = k - 1
        f = 1
        for node in g[p]:
            if d[node] != -2:
                f *= t
                f %= MOD
                t -= 1
                res *= d[node]
                res %= MOD
        d[p] = res * f
print(d[0] * k % MOD)
