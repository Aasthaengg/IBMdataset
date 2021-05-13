from itertools import permutations
N, C = map(int, input().split())

d = [[0]*C for i in range(C)]
for i in range(C):
  d[i] = [int(c) for c in input().split()]

grid = [[0]*C for i in range(3)]
for i in range(N):
  inf = [int(c)-1 for c in input().split()]
  for j in range(N):
    x = (j+i+2)%3
    g = inf[j]
    grid[x][g] += 1

record = [[0]*C for i in range(3)]
for i in range(3):
  for j in range(C):
    m = 0
    for h in range(C):
      m += grid[i][h]*d[h][j]
    record[i][j] = m

ans = 10**9
seq = range(C)
for i,j,h in permutations(seq,3):
  m = record[0][i]+record[1][j]+record[2][h]
  if m<ans:
    ans = m
    
print(ans)