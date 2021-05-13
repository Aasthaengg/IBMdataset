import math
N = int(input())
if math.log10(N)%1 != 0:
  K = str(N)
  ans = 0
  for i in range(len(K)):
    ans += int(K[i])
  print(ans)
else:
  print(10)