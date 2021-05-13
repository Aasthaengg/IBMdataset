f=lambda:map(int,input().split())
n,k=f()
l=list(f())
v=0
m=min(n,k)
from bisect import *
for i in range(m+1):
  for j in range(m+1-i):
    s=sorted(l[:i]+l[n-j:])
    v=max(v,sum(s[min(bisect_left(s,0),k-i-j):]))
print(v)