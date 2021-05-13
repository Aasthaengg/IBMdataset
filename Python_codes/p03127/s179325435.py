import math
N = int(input())
A = list(map(lambda a: int(a), input().split(" ")))

gcd = A[0]
for i in range(len(A)):
  gcd = math.gcd(gcd, A[i])
  
print(gcd)
