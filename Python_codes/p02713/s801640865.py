import math
N = int(input())
ans = 0
for i in range(1,N+1):
  for j in range(1,N+1):
    for k in range(1,N+1):
      temp = math.gcd(i,j)
      temp = math.gcd(temp,k)
      ans += temp
print(ans)