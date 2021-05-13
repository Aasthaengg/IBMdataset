import math
s = input().split()
n=int(s[0])
m=int(s[1])
l=0
r=float('inf')
for i in range(m):
    s = list(map(int,input().split()))
    l=max(l,s[0])
    r=min(r,s[1])
a=r-l
if a>=0:
    print(a+1)
else:
    print(0)
