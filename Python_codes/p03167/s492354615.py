MOD = pow(10,9) + 7
H, W = map(int,raw_input().split())

grid = [[0]*W for h in range(H)]
grid[0][0] = 1

for h in range(H) :  
  row = raw_input()

  for w in range(W) :
    if row[w] == '#' : continue
    if h > 0 : grid[h][w] += grid[h-1][w]
    if w > 0 : grid[h][w] += grid[h][w-1]
    grid[h][w] %= MOD
  
print grid[-1][-1] % MOD