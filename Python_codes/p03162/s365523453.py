import math
N = int(input())
point_table = []
for _ in range(N):
  a,b,c = map(int, input().split())
  point_table.append([a, b, c])

dp_list = [[0] * 3 for _ in range(N)]
dp_list[0] = point_table[0].copy()

for i in range(N - 1):
  for j in range(3):
    for k in range(3):
      if j != k:
        cost = dp_list[i][j] + point_table[i + 1][k]
        if cost > dp_list[i + 1][k]:
          dp_list[i + 1][k] = cost

print(max(dp_list[-1]))