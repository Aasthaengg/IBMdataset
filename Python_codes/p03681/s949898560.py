import math
mod=10**9+7
n,m=map(int,input().split())
if n+1<m or m+1<n:
    print(0)
    exit()
elif n==m:
    print((2*math.factorial(n)**2)%mod)
else:
    print((math.factorial(n)*math.factorial(m))%mod)

