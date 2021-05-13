import math
n=int(input())
result=0
for i in range(1,n+1):
  for j in range(1,n+1):
    num=math.gcd(i,j)
    for k in range(1,n+1):
      result+=math.gcd(num,k)
print(result)