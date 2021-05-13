from collections import deque, defaultdict

inf = 10**15
h, w = map(int, input().split())
#隣接リスト
#G = defaultdict(lambda:[])
G = [[inf]*(h*w) for _ in range(h*w)]
#################################

def warshall_floyd(d):
    #d[i][j]:iからjに行く最短経路
    for k in range(h*w):
        for i in range(h*w):
            for j in range(h*w):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d
  
li = []
for j in range(h):
    g = list(input())
    temp = []
    for i in g:
      if i=='.':
        temp.append(0)
      else:
        temp.append(1)
    li.append(temp)
for i in range(h):
    for j in range(w-1):
        if li[i][j]==0 and li[i][j+1]==0:
            G[i*w+j][i*w+j+1] = 1
            G[i*w+j+1][i*w+j] = 1
            G[i*w+j][i*w+j] = 0
            G[i*w+j+1][i*w+j+1] = 0
for i in range(h-1):
    for j in range(w):
        if li[i][j] ==0 and li[i+1][j]==0:
            G[i*w+j][i*w+w+j] = 1
            G[i*w+j+w][i*w+j] = 1
            G[i*w+j+w][i*w+j+w] = 0
            G[i*w+j][i*w+j] = 0
    
#################################
d = warshall_floyd(G)
max_ = 0
for i in range(h*w):
  for j in range(h*w):
    if d[i][j] < inf:
      max_ = max(max_, d[i][j])
print(max_)