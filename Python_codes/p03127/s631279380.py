import math

n = int(input())
A = list(map(int,input().split()))

ans = math.gcd(A[0],A[1])
for i in range(2,n):
    ans = math.gcd(ans, A[i])
    
print(ans)