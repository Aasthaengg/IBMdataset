def root(x):
    if r[x] < 0:
        return x
    else:
        r[x] = root(r[x])
        return r[x]
def unite(x, y):
    x = root(x)
    y = root(y)
    if x != y:
        if r[x] > r[y]:
            x,y = y,x
        r[x] += r[y]
        r[y] = x
n,m = map(int,input().split())
r = [-1] * n
for i in range(m):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    unite(a,b)
ans = 0
for i in r:
    if i < 0:
        ans += 1
print(ans-1)
