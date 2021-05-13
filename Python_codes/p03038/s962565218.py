n,m=map(int,input().split())
from collections import Counter as co
d=co(list(map(int,input().split())))
for i in range(m):
    b,c=map(int,input().split())
    if c in d:d[c]+=b
    else:d[c]=b
f=sorted(d.items(),reverse=1)

now =0
s=0
for k,v in f:
    if now+v<=n:
        now+=v
        s+=k*v
    else:
        
        print(s+(n-now)*k);exit()
