INF = 10**10
n,m,R = map(int,input().split())
r=list(map(int,input().split()))
for i in range(R):
    r[i]-=1
d = [[INF]*n for i in range(n)] 
# 入力
for i in range(m):
    a,b,c = map(int,input().split())
    a,b = a-1, b-1
    d[a][b] = c
    d[b][a] = c # 無向グラフ
for i in range(n):
    d[i][i] = 0

def FW():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
FW()
from itertools import permutations, combinations
ans=INF
for v in permutations(r):
    tmp=0
    for i in range(R-1):
        tmp+=d[v[i]][v[i+1]]
    ans=min(ans,tmp)
print(ans)