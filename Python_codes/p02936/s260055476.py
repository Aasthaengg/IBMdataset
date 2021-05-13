import sys
sys.setrecursionlimit(10**7)
 
N, Q = map(int, input().split())
graph = [[] for i in range(N)]
cnt = [0]*N

# 入力しながらグラフを作成
for i in range(N-1):
  a, b = map(int, input().split())
  a, b = a-1, b-1
  graph[a].append(b)
  graph[b].append(a)

# 初期値を設定
for i in range(Q):
  p, x = map(int, input().split())
  cnt[p-1] += x

v = [False]*N

# stack=[]
def dfs(n,prv):
  # stack.append(n)
  if v[n]: return
  cnt[n] += prv
  v[n] = True
  for nv in graph[n]:
    dfs(nv, cnt[n])
   
dfs(0,0)
print(*cnt)
# print(stack)