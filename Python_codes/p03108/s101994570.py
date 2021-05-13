maxn = 100000

n , m = map(int, input().split())

par = [0] * n
rank = [0] * n
siz = [1] * n

#初期化
for i in range(n):
    par[i] = i
    rank[i] = 0

#判定(一番上野根を求める)
def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]
    
#結合
def unite(x , y):
    rx = find(x)
    ry = find(y)
    
    if rx == ry:
        return
    
    if rank[rx] < rank[ry]:
        par[rx] = ry
        siz[ry] += siz[rx]
        siz[rx] = 0
    elif rank[rx] > rank[ry]:
        par[ry] = rx
        siz[rx] += siz[ry]
        siz[ry] = 0
    else:
        par[ry] = x
        siz[rx] += siz[ry]
        siz[ry] = 0
        rank[rx] += 1

a = [0] * m
b = [0] * m
for i in range(m):
    a[i],b[i] = map(int,input().split())
    a[i] -= 1
    b[i] -= 1
    
nn = [0]*(maxn+1)
for i in range(maxn+1):
    nn[i] = i * (i-1) // 2
    
dis = [0]*m
ans = n*(n-1) // 2
dis[m-1] = ans
for i in range(m-1,0,-1):
    if find(a[i]) == find(b[i]):
        dis[i-1] = ans
    else:
        ans -= (siz[find(a[i])] * siz[find(b[i])])
        dis[i-1] = ans
        
    unite(a[i],b[i])
    
for i in range(m):
    print(dis[i])