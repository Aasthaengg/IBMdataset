import math

n = int(input())
ans = 0
if n== 0:
  print(0)
  exit()
m = math.floor(math.log(n,5))

if n%2 == 1:
  print(0)
else:
  for j in range(1,m+1):
    ans += n//((5**j)*2)
    
    
  print(ans)