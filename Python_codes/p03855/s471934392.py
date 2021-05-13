maxn = 2 * (10**5)

n , k , l = map(int, input().split())

par = [[0] * (n+1) for _ in range(2)]
rank = [[0] * (n+1) for _ in range(2)]

#初期化
for i in range(n+1):
    par[0][i] = i
    rank[0][i] = 0
    par[1][i] = i
    rank[1][i] = 0

#判定(一番上野根を求める)
def find(num,x):
    if par[num][x] == x:
        return x
    else:
        par[num][x] = find(num,par[num][x])
        return par[num][x]
    
#結合
def unite(num , x , y):
    rx = find(num,x)
    ry = find(num,y)
    
    if rx == ry:
        return
    
    if rank[num][rx] < rank[num][ry]:
        par[num][rx] = ry
    elif rank[num][rx] > rank[num][ry]:
        par[num][ry] = rx
    else:
        par[num][ry] = x
        rank[num][rx] += 1
        

for i in range(k):
    p,q = map(int, input().split())
    unite(0,p,q)
        
for i in range(l):
    r,s = map(int, input().split())
    unite(1,r,s)
    
pairs = [(find(0,i),find(1,i)) for i in range(1,n+1)]
from collections import Counter
pairc = Counter(pairs)
ans = [pairc[pair] for pair in pairs]

print(*ans)