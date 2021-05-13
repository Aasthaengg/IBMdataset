n,m=map(int,input().split())
side=[]
for i in range(m):
    a,b=map(int,input().split())
    side.append((a-1,b-1))

#Union-Find
#xの根を求める
def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]
#xとyの属する集合の併合
def unite(x,y):
    x = find(x)
    y = find(y)
    
    if x == y:
        return False
    else:
        #sizeの大きいほうがx
        if par[x] > par[y]:
            x,y = y,x
        par[x] += par[y]
        par[y] = x
        return True

#xとyが同じ集合に属するかの判定
def same(x,y):
    return find(x) == find(y)

#xが属する集合の個数
def size(x):
    return -par[find(x)]


ans=0
for i in range(m):
    #初期化
    par = [-1]*n
    for j in range(m):
        if j==i:
            continue
        else:
            unite(side[j][0],side[j][1])
    if not same(side[i][0],side[i][1]):
        ans+=1
print(ans)