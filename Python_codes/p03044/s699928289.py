n=int(input())

#隣接リスト表現
es=[[] for i in range(n)]
for i in range(n-1):
  u,v,w=list(map(int,input().split()))
  es[u-1].append([v-1,w])
  es[v-1].append([u-1,w])


# 再帰の深さが1000を超えそうなときはこれをやっておく
import sys
sys.setrecursionlimit(10**7)

#頂点vから初めて白なら１、黒なら−１、未探索なら０
colors=[0 for i in range(n)]
def search(v,color):
  colors[v]=color
  #vから行ける辺について考える
  for to in es[v]:
    if colors[to[0]]==0 and to[1]%2==0:
      search(to[0],color)
    elif colors[to[0]]==0 and to[1]%2==1:
      search(to[0],-color)
  return colors

search(0,1)
for i in colors:
  if i==-1:
    print(0)
  else:
    print(1)
    
  
  

