n,k=map(int,input().split())
a=list(map(int,input().split()))
aa=min(a)
n-=k
import math
q=0
if n%(k-1)==0:
    q+=n//(k-1)
else:
    q+=n//(k-1)+1
print(q+1)