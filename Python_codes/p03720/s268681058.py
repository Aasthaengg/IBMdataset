N, M = map(int, input().split())
city = [0] * N
for i in range(M):
  a, b = map(int, input().split())
  city[a - 1] += 1
  city[b - 1] += 1
for i in range (N):
  print(city[i])