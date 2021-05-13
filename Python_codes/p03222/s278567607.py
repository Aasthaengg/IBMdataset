from collections import deque
from copy import deepcopy

H, W, K = map(int, input().split())

mod = int(1e9+7)

## 一列の中で可能な置換を全て保持しておく
perm_lst = []
def bfs():
    dq = deque() ## ((post permutation), next_line)
    dq.append(([],0))
    while dq:
        post, line = dq.popleft()
        if line < W: ## 何も繋がない
          post_tmp = deepcopy(post) ## もっといい書き方ありそう
          post_tmp.append((line,line))
          dq.append( (post_tmp,line+1) )
        if line < W-1: ## 隣とつなぐ
          post_tmp = deepcopy(post) ## もっといい書き方ありそう
          post_tmp.append((line,line+1))
          dq.append( (post_tmp,line+2) )
        if line == W:
          perm_lst.append(post)
bfs()
#print(perm_lst)

## dp[i][j]: i列目まで線を引いてjにいる場合の数の総数
dp = [[0 for j in range(W)] for i in range(H+1)]
dp[0][0] = 1
for i in range(1,H+1):
  for perm in perm_lst:
    for j in range(len(perm)):
      if perm[j][0] != perm[j][1]:
        dp[i][perm[j][0]] += dp[i-1][perm[j][1]]
        dp[i][perm[j][1]] += dp[i-1][perm[j][0]]
      else:
        dp[i][perm[j][0]] += dp[i-1][perm[j][0]]
      
#print(dp)

print(dp[H][K-1] % mod)