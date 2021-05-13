import math

n = int(input())

def solve():
  for k in range(2, int(math.sqrt(n)) + 1):
    if n % k == 0:
      return False
  
s = solve()
if s != False:
  print(n-1)
  exit()
  
ans = 10**12
for k in range(2, int(math.sqrt(n)) + 1):
  if n % k == 0:
    ans = min(ans,k+n//k)
  
print(ans-2)

