# -*= coding: utf-8 -*-
from collections import deque

N, X, Y = map(int, input().split())

d = deque() # 初期化

ans = [0] * N

# BFS
for i in range(N):
  # 0 〜 N-1の各頂点からスタート
  
  cost = [-1] * N
  cost[i] = 0
  d.append(i) # 基準とする頂点をノードiにする
  
  while len(d) > 0:
    # dequeueが空でない間ループ
    
    # 現在のノードのインデックス
    current = d.popleft()
    
    if current - 1 >= 0 and cost[current - 1] == -1:
      # 1つ前のノードを登録
      
      d.append(current - 1)
      cost[current - 1] = cost[current] + 1
      
    if current + 1 < N and cost[current + 1] == -1:
      # 1つ後ろのノードを登録
      
      d.append(current + 1)
      cost[current + 1] = cost[current] + 1
      
    if current == X - 1 and cost[Y - 1] == -1:
      # XからYへのルートを登録
      
      d.append(Y - 1)
      cost[Y - 1] = cost[current] + 1
    
    if current == Y - 1 and cost[X - 1] == -1:
      # YからXへのルートを登録
      
      d.append(X - 1)
      cost[X - 1] = cost[current] + 1
      
  # この時点でcostにはノードiから各ノードへの最小コストが格納されている
  
  #print(cost)
  for j in range(N):
    ans[cost[j]] += 1

for i in range(1, N):
  print(ans[i]//2) # ノードA→Bと、逆向きのB→Aが、両方カウントされているので2分の1する