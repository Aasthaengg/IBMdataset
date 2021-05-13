# スタート地点からDFSで大きい順に入れていけば、最も大きい数以外は得点を得られる

N = int(input())
E = [[] for i in range(N)]
for i in range(N-1):
  a,b = map(int,input().split())
  E[a-1].append(b-1)
  E[b-1].append(a-1)

# 得点を大きい順に並べる
C = sorted(list(map(int,input().split())))[::-1]

ans = [-1 for i in range(N)] # -1は未訪問
point = sum(C[1:])

from collections import deque
q = deque([])
q.append(0)
ind = 0
while q:
  v = q.popleft()
  if ans[v] != -1:
    # 訪問済み
    continue
  ans[v] = C[ind]
  ind += 1
  if ind == len(C):
    break
  children = E[v]
  for child in children:
    q.append(child)
  
print(point)  
print(*ans)