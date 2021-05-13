H,W = map(int,input().split())
mod = 10**9 + 7
grid_0 = [0] * (W+1)
grid_0[1] = 1

for n in range(1,H+1):
  grid_1 = [0] * (W+1)
  for i, j in enumerate(input(), 1):
    if j == ".":
      grid_1[i] = (grid_0[i] + grid_1[i-1]) % mod
  grid_0 = grid_1

print(grid_0[-1])