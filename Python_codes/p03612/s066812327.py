import numpy as np
n=int(input())
p=list(map(int,input().split()))

arr=np.array(p)
temp=np.arange(1,n+1)
zeroplace=arr-temp
a=np.nonzero(zeroplace==0)[0].tolist()

cnt=len(a)
for i in range(1,len(a)):
    if a[i-1]+1==a[i]:
        a[i]-=1
        cnt-=1
print(cnt)