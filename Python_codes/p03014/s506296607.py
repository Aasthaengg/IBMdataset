import sys

input = sys.stdin.readline

H, W = map(int, input().split())

grid = []

count_w = [[0] * W for _ in range(H)]
count_h = [[0] * W for _ in range(H)]

for _ in range(H):
  grid.append([x for x in input()])
  

for h in range(H):
  r = 0
  count = 0
  for l in range(W):
    while r < W and grid[h][r] == '.':
      r += 1
      count += 1
    count_w[h][l] = count
    if r == l:
      r += 1
      count = 0
      
for w in range(W):
  r = 0
  count = 0
  for l in range(H):
    while r < H and grid[r][w] == '.':
      r += 1
      count += 1
    count_h[l][w] = count
    if r == l:
      r += 1
      count = 0

answer = 0

for h in range(H):
  for w in range(W):
    answer = max(answer, count_h[h][w] + count_w[h][w] - 1)

print(answer)
