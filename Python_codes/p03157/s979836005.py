def root(x):
    i,j = x[0],x[1]
    if (i,j) == p[i][j]:
        return (i,j)
    y = root(p[i][j])
    p[i][j]=y
    return y
def unite(x, y):
    px = root(x); py = root(y)
    if px == py:
        return 0
    pxi,pxj= px[0],px[1];pyi,pyj= py[0],py[1];
    rx = rank[pxi][pxj]; ry = rank[pyi][pyj]
    if ry < rx:
        p[pyi][pyj] = px
    elif rx < ry:
        p[pxi][pxj] = py
    else:
        p[pyi][pyj] = px
        rank[pxi][pxj] += 1
    return 1

h,w = map(int, input().split( ))
s = ["x"*(w+2)]+["x"+input()+"x" for _ in range(h)]+["x"*(w+2)]
p = [[(i,j) for j in range(w+2)] for i in range(h+2)]
rank = [[1]*(w+2) for _ in range(h+2)]

tonari = [(-1,0),(1,0),(0,1),(0,-1)]
for i in range(1,h+1):
    for j in range(1,w+1):
        for di,dj in tonari:
            i2 = i+di;j2 = j+dj
            if (s[i][j],s[i2][j2])==("#",".") or (s[i][j],s[i2][j2])==(".","#") :
                unite((i,j),(i2,j2))
c = [[p[i][j] for j in range(1,w+1)] for i in range(1,h+1)]
ans = 0
####
for i in range(h+2):
    for j in range(w+2):
        root((i,j))
pb = {}
pw = {}
##pb,pwの引数はroot とる
for i in range(h):
    for j in range(w):
        k = c[i][j]
        if s[i+1][j+1] =="#":
            if root(k) in pb:
                pb[root(k)]+=1
            else:
                pb[root(k)]=1
        elif s[i+1][j+1]==".":
            if root(k) in pw:
                pw[root(k)]+=1
            else:
                pw[root(k)]=1
ans = 0
c2 =  set([p[i][j] for j in range(w+2) for i in range(h+2)])

for k in c2:
    if k in pb and k in pw:
        ans += pb[k]*pw[k]
print(ans)
