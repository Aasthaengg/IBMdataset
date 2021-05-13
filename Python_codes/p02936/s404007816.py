# 再帰の深さが1000を超えそうなときはこれをやっておく
import sys
sys.setrecursionlimit(10**7)
#隣接リスト表現
n,q=list(map(int,input().split()))
es=[[] for i in range(n)]
for i in range(n-1):
  a,b=list(map(int,input().split()))
  es[a-1].append(b)
  es[b-1].append(a)
#頂点に値をたす
cnt=[0 for i in range(n)]
for i in range(q):
  p,x=list(map(int,input().split()))
  cnt[p-1]=cnt[p-1]+x
  
#頂点vから始めるdfsで累積和をを求める
#check=訪れたことがあるかどうかを探索
check=[0 for i in range(n)]
def dfs(v):
  check[v-1]=1
  for l in es[v-1]:
    if check[l-1]==0:
      cnt[l-1]=cnt[l-1]+cnt[v-1]
      dfs(l)
  return cnt
#出力
dfs(1)
for i in cnt:
  print(i,end=" ")
  

