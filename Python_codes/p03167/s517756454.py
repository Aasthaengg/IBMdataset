from collections import deque

H,W=map(int,input().split())
mod=10**9+7
S=[]
for i in range(H):
  S.append(input())
  
total = [[0 for i in range(W)] for j in range(H)]
total[0][0] = 1

now = (0,0)
for i in range(H):
  for j in range(W):
    if S[i][j] == '#':continue
    if i > 0 and S[i-1][j] != '#':
      total[i][j] += total[i-1][j]
    if j > 0 and S[i][j-1] != '#':
      total[i][j] += total[i][j-1]
    total[i][j] %= mod
        
print(total[-1][-1]%mod)