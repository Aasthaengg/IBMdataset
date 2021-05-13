from math import *
n,k=map(int,input().split())
s=ceil(n/2)
if(s>=k):
    print("YES")
else:
    print("NO")