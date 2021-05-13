def solve(n, m, a, b):
    E = {i: [] for i in range(n)}
    for u, v in zip(a, b):
        u, v = u-1, v-1
        E[u].append(v)
        E[v].append(u)
    L = list(range(n))
    for s in range(n):
        if L[s] == s:
            L[s] = s
            que = [s]
            while que:
                u = que.pop(0)
                for v in E[u]:
                    if L[v] != s:
                        L[v] = s
                        que.append(v)
    return len(set(L)) - 1
 
n, m = map(int, input().split())
if m == 0:
    a, b = [], []
else:
    a, b = zip(*[map(int, input().split()) for i in range(m)])
print(solve(n,m,a,b))