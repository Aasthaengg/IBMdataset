import math
N,M = map(int,input().split())

sq = math.sqrt(M)
sq = math.floor(sq)


ans = 1
for i in range(1,sq+2):
  if M % i == 0:
    if i * N <= M:
      ans = max(i,ans)
    if M / i * N <= M:
      ans = max(M // i,ans)
if N == 1:
  print(int(M))
else:
  print(int(ans))
