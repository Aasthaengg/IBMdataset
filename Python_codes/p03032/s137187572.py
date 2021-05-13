n,k,*l=map(int,open(0).read().split())
v,m=0,min(n,k)+1
from bisect import*
for i in range(m):
  for j in range(m-i): s=sorted(l[:i]+l[n-j:]); v=max(v,sum(s[min(bisect(s,-1),k-i-j):]))
print(v)