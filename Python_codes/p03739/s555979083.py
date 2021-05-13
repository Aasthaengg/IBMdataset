import copy
n=int(input())
a=[0]+list(map(int,input().split()))
b=copy.copy(a)
psum=0
nsum=0
sum1=0
sum2=0
for i in range(1,n+1):
    if i%2!=0:
        psum+=max([0,1-sum1-a[i]])
        a[i]+=max([0,1-sum1-a[i]])
        sum1+=a[i]
    else:
        psum+=max([0,1+sum1+a[i]])
        a[i]-=max([0,1+sum1+a[i]])
        sum1+=a[i]
for i in range(1,n+1):
    if i%2!=0:
        nsum+=max([0,1+sum2+b[i]])
        b[i]-=max([0,1+sum2+b[i]])
        sum2+=b[i]
    else:
        nsum+=max([0,1-sum2-b[i]])
        b[i]+=max([0,1-sum2-b[i]])
        sum2+=b[i]

print(min([psum,nsum]))
