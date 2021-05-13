import sys
input = sys.stdin.readline
# warshall_floyd法
def warshall_floyd(d,n):
 for k in range(n):
  for i in range(n):
   for j in range(n):
    d[i][j]= min(d[i][j],d[i][k]+d[k][j])
 return d

H,W = map(int,input().split())
# 隣接行列の定義、初期化
# ①コスト(存在しないときはinf)
d = [0 for i in range(10)]
# ②自分自身へのコストは０
for i in range(10):
 d[i] = list(map(int,input().split()))
ct=[0]*11
for i in range(H):
  lst=list(map(int,input().split()))
  for j in range(W):
   ct[lst[j]+1]+=1

A=warshall_floyd(d,10)
ans=0
for i in range(10):
 ans+=ct[(i+1)]*A[i][1]
print(ans)
