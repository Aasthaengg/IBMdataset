import math

n,d = map(int,input().split())
LO = d+1+d
print(math.ceil(n/LO))