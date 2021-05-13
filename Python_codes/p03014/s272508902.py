H,W = map(int,input().split())
G=[input() for _ in range(H)]
A_u=[[0 for _ in range(W)] for _ in range(H)]
A_d=[[0 for _ in range(W)] for _ in range(H)]
A_r=[[0 for _ in range(W)] for _ in range(H)]
A_l=[[0 for _ in range(W)] for _ in range(H)]
for h in range(H):
  for w in range(1,W):
    if G[h][w-1] == '.':
      A_r[h][w] = A_r[h][w-1]+1
  for w in range(W-2,-1,-1):
    if G[h][w+1] == '.':
      A_l[h][w] = A_l[h][w+1]+1
for w in range(W):
  for h in range(1,H):
    if G[h-1][w] == '.':
      A_d[h][w] = A_d[h-1][w]+1
  for h in range(H-2,-1,-1):
    if G[h+1][w] == '.':
      A_u[h][w] = A_u[h+1][w]+1
ans=0
for h in range(H):
  for w in range(W):
    if G[h][w] == '.':
      ans = max(ans,A_r[h][w]+A_l[h][w]+A_d[h][w]+A_u[h][w]+1)
print(ans)