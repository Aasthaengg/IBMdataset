import math
n,k=map(int,input().split())
A=list(map(int,input().split()))
if n==k:
    print(1)
else:
    n-=k
    print(1+math.ceil(n/(k-1)))