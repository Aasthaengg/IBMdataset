
N = int(input())
A = list(map(int,input().split()))
import math

f = A[0]
for i in range(1,N):
    a,b=f, A[i]
    f=math.gcd(a,b)

print(f)
