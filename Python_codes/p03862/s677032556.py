n,x=map(int,input().split())

a=list(map(int,input().split()))

import copy
b = copy.deepcopy(a) 

#a[0]から貪欲
i=1
cnt=0
while i<n:
    if a[i]+a[i-1]>x:
        tmp=(a[i]+a[i-1])-x
        cnt+=tmp
        a[i]=max(0,a[i]-tmp)
    i+=1

#a[n-1]から貪欲
b=b[::-1]
i=1
cnt1=0
while i<n:
    if b[i]+b[i-1]>x:
        tmp=(b[i]+b[i-1])-x
        cnt1+=tmp
        b[i]=max(0,b[i]-tmp)
    i+=1

print(min(cnt,cnt1))