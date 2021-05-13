import math
N, M = map(int, input().split())

ans = 0

if N > math.floor(M / 2):
  ans = math.floor(M / 2)
else:
  ans = N + math.floor((M - N * 2) / 4)

print(ans)