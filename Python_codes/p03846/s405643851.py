n=int(input())
a=list(map(int,input().split()))
x=[0]*(n+1)
p=10**9+7
for i in a:
   x[i]+=1
if n%2==0:
    m=n//2
    f=0
    for i in range(m):
        if x[2*i+1]!=2:
            f=1
    if f==1:
        print(0)
    else:
        print(pow(2,m,p))
else:
    m=n//2
    f=0
    if x[0]!=1:
        f=1
    for i in range(m):
        if x[2*i+2]!=2:
            f=1
    if f==1:
        print(0)
    else:
        print(pow(2,m,p))
