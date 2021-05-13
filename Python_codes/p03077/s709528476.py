n=int(input())
ar=[]
for _ in range(5):
    ar.append(int(input()))
m=min(ar)
from math import ceil
k=ceil(n/m)
print(k+4)