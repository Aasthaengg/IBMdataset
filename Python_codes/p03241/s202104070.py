import math
N, M = map(int, input().split())

ans = 1
if(N < M//N):
  i = N
  while(ans == 1 and i <= math.sqrt(M)):
    if(M % i == 0):
      ans = M//i
    i += 1
if(N >= M//N or ans == 1):
  i = M//N
  while(ans == 1 and i >= 1):
    if(M % i == 0):
      ans = i
    i -= 1
  
print(ans)