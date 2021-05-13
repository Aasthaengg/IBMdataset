import math
n,k=map(int,input().split())
a=list(map(int,input().split()))

b=math.ceil((n-1)/(k-1))
print(b)