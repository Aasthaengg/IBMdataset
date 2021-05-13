import numpy as np
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

c=[]
need=sum(a)-sum(b)
ans=0
for i in range(n):
    c.append(a[i]-b[i])
    
c=sorted(c)
arr=np.array(c)
arr2=arr[arr>=0]
d=arr2.tolist()
#print(need,d)
for i in range(len(d)):
    need-=d[i]
    if need>=0:
        ans+=1
#print(ans)
if sum(a)<sum(b):
    print(-1)
else:
    print(n-ans)