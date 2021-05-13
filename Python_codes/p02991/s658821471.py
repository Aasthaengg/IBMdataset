N,M=map(int, input().split())
u=[0]*M
v=[0]*M
for i in range(M):
  u[i],v[i] = map(int, input().split())
S,T=map(int, input().split())

edges = []
for i in range(M):
  edges.append([u[i]*3-3, v[i]*3-2])
  edges.append([u[i]*3-2, v[i]*3-1])
  edges.append([u[i]*3-1, v[i]*3-3])

def edges_to_pt(edges,n):
  '''
  input
    edges: 枝の[始点,終点]を格納した2次元配列　edges=[[0,1],[1,2],[2,0]]
    n:  頂点数 n=3

  output
    pt: 各点との結合場所を格納した2次元配列 pt=[[1],[2],[0]]
  '''
  pt = [[] for i in range(n)]
  while edges:
    temp_edge = edges.pop()
    pt[temp_edge[0]].append(temp_edge[1])
  return pt

def bfs(pt,v):
  '''
  input
    pt: 各点との結合場所を格納した2次元配列　pt=[[1, 2, 3], [0], [5, 0], [6, 0], [6], [2], [3, 4]]
    v: 初期点 v=0

  output
    d: 初期点からの距離を格納した配列 d=[0, 1, 1, 1, 3, 2, 2]
  '''
  n=len(pt)
  d=[-1]*n
  d[v]=0
  q=[v]
  c=1
  while q:
    q1=[]
    for i in q:
      for j in pt[i]:
        if d[j]==-1:
          d[j]=c
          q1.append(j)
    q=q1
    c+=1
  return d

pt = edges_to_pt(edges,3*N)
ans = bfs(pt,3*S-3)[3*T-3] // 3

if ans == -1:
  print(-1)
else:
  print(ans)