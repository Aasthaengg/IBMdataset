from collections import *
N, K, L = map(int,input().split())

def f(m):
    *a, = range(N)
    def g(i):
        if a[i] == i:
            return i
        a[i] = g(a[i])
        return a[i]
    for _ in range(m):
        p, q = map(int,input().split())
        a[g(q-1)] = g(p-1)
    return g

x, y = f(K), f(L)
c = Counter((x(i),y(i)) for i in range(N))
print(*((c[x(i),y(i)]) for i in range(N)))
