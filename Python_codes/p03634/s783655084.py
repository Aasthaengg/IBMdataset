from sys import stdin
import sys
input = stdin.readline
sys.setrecursionlimit(10**6)
mod = 10**9+7
 
n = int(input())
m = n-1
graph = [[] for j in range(n)]
d = {}

for i in range(m):
    a,b,c = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
    d[(a-1,b-1)] = d[(b-1,a-1)] = c

q,k = map(int,input().split())
    
# 頂点kから各頂点への距離
dis = [0]*n
    
# v = 現在の頂点
# per = vの親(vが根のときは-1)
# ans = 総距離
def DFS(v,per,ans):
	if not per == -1 :
		dis[v] = ans
	for i in graph[v]:
        # 移動先iがvの親ならスキップ（訪問済みのチェックと同じ）
		if i == per :
			continue
		DFS(i,v,ans+d[(v,i)])

DFS(k-1,-1,0)

for i in range(q) :
  x,y = map(int,input().split())
  print(dis[x-1]+dis[y-1])