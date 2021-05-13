import math
n = int(input())
ans = 10**12
for i in range(1,int(math.sqrt(n)+1)):
  if n % i== 0:
    num = (n//i)+ i-2
  ans = min(ans,num)
print(ans)