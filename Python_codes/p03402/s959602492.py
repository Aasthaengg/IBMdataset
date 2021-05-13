AB = tuple(map(int, input().split()))
WB = ".#"

grid = [[[WB[-1-i]]*100 for _ in range(50)] for i in range(2)]

for i in range(2):
  H, W = divmod(AB[i]-1, 50)
  for h in range(H):
    for j in range(50):
      grid[i][2*h+i][2*j] = WB[i]
  for w in range(W):
    grid[i][2*H+i][2*w] = WB[i]

print(100, 100)
for G in grid:
  for ans in G:
    print("".join(ans))