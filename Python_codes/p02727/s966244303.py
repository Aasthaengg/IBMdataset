X, Y, R, G, N = map(int, input().split())
r = [int(x) for x in input().split()]
g = [int(x) for x in input().split()]
n = [int(x) for x in input().split()]
r = sorted(r)[R-X:]
g = sorted(g)[G-Y:]
n = sorted(n, reverse=True)

nr = 0; ng = 0; nn = 0
for i in range(N):
    if n[nn] <= min(r[nr], g[ng]):
        break
    if r[nr] < g[ng]:
        r[nr] = n[nn]
        nr += 1
        if nr == X:
            nr = X-1
    else:
        g[ng] = n[nn]
        ng += 1
        if ng == Y:
            ng = Y-1
    nn += 1

print(sum(r) + sum(g))