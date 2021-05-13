h,w = map(int,input().split())
s = [input() for _ in range(h)]

#union-find

n = h*w

par = [0] * n
rank = [0] * n

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
    elif rank[rx] > rank[ry]:
        par[ry] = rx
    else:
        par[ry] = x
        rank[rx] += 1

for i in range(h):
    for j in range(w-1):
        if s[i][j] != s[i][j+1]:
            unite(i*w+j , i*w +j+1)
            
for i in range(h-1):
    for j in range(w):
        if s[i][j] != s[i+1][j]:
            unite(i*w+j , (i+1)*w +j)
            
uni = [[0]*2 for _ in range(n)]

for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            k = 0
        else:
            k = 1
        uni[find(i*w+j)][k] += 1
        
ans = 0
for i in uni:
    ans += i[0] * i[1]
    
print(ans)