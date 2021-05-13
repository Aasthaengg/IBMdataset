def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]
def unite(x,y):
    x = find(x)
    y = find(y)
    if x == y: return False
    #sizeの大きいほうがx
    if par[x] > par[y]: x,y = y,x
    par[x] += par[y]
    par[y] = x
    return True

n, m = map(int, input().split())
ab = []
ans = m
for _ in range(m):
    a, b = map(int, input().split())
    ab.append([a-1, b-1])
for i in range(m):
    par = [-1]*n
    for j in range(m):
        if i==j: continue
        unite(ab[j][0], ab[j][1])
    if -min(par) == n: ans -= 1
print(ans)