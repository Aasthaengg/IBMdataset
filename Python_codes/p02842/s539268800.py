import math

n = int(input())
ans = int(n / 1.1)
while True:
  if math.floor(ans * 1.08) == n:
    break
  ans += 1
  
  if ans > n:
    break
if ans > n:
  print(':(')
else:
  print(ans)