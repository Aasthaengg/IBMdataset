import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import bellman_ford
from scipy.sparse.csgraph import connected_components

N,M = map(int,input().split())
ABC = [list(map(int,input().split())) for _ in range(M)]

row, col, val = zip(*ABC)
# -1倍しておいて最短路問題にする
val = [-(x) for x in val]
graph = csr_matrix((val,(row,col)),(N+1,N+1))

# 強連結成分に制限。ここに負閉路があればinf～
find_component_graph = csr_matrix(([1]*(M+1),(row+(N,),col+(1,))),(N+1,N+1))
# n = 個数、label=各頂点が属する連結成分のラベル[0,0,1,1,1]
n, labels = connected_components(find_component_graph,connection = 'strong')
idx = (labels == labels[1]) # [False, False, True~]
graph = graph[idx,:][:,idx]

try:
  dist = bellman_ford(graph,indices = [0])[0].astype(int)
  answer = -dist[-1]
except:
  answer = 'inf'

print(answer)