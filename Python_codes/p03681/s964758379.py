import math

n,m=map(int,input().split())

if abs(n-m)>1:
    print(0)
elif abs(n-m)==1:
    print((math.factorial(max(n,m))*math.factorial(min(n,m)))%(10**9+7))
else:
    print((2*math.factorial(n)*math.factorial(m))%(10**9+7))
