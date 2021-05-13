import math

N = int(input())
n = 0
m = 0
res =0 
List1 = ["INF"]*(N+1)
for i in range(1,N+1):
  for j in range(1,N+1):
    n = math.gcd(i,j)
    if List1[n] == "INF":
      for k in range(1,N+1):
        m += math.gcd(n,k)
      res += m
      List1[n] = m
      m = 0
    else:
      res += List1[n]
print(res)