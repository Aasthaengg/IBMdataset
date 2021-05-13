n, q = map(int, input().split())

par = [i for i in range(n + 1)]

def find(x):
    if x == par[x]:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    par[x] = y

def same(x, y):
    return find(x) == find(y)

for i in range(q):
    a, b = map(int, input().split())
    unite(a, b)

for i in range(n):
    find(i+1)

par.pop(0)

al = set(par)
print(len(al) - 1)
