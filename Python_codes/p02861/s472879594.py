from math import sqrt
N = int(input())
D = [list(map(int, input().split())) for i in range(N)]
total = 0
for i in range(N):
  for j in range(N):
    if i != j:
      total += sqrt((D[i][0] - D[j][0]) ** 2 + (D[i][1] - D[j][1]) ** 2)
print(total / N)