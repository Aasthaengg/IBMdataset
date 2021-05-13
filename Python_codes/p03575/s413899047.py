N, M = map(int, input().split())
E = [[int(x) - 1 for x in input().split()] for _ in range(M)]

def root(par, a):
    a_ = a
    while par[a] != a:
        a = par[a]
    par[a_] = a
    return a

def unite(par, a, b):
    ar = root(par, a)
    br = root(par, b)
    if ar != br:
        par[ar] = br

ans = 0
for i in range(M):
    par = list(range(N))
    for j in range(M):
        if i == j:
            continue
        a, b = E[j]
        unite(par, a, b)

    r0 = root(par, 0)
    for k in range(1, N):
        if root(par, k) != r0:
            ans += 1
            break
print(ans)