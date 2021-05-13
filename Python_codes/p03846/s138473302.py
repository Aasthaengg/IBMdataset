t = int(input())
m = list(map(int,input().split()))
q={}
mod=10**9+7
z=False
cnt0=0
for i in range(t):
    d=m[i]
    a=(t-1-d)//2
    if d==0:
        cnt0+=1
    if (a,a+d) not in q:
        q[(a,a+d)]=0
    q[(a,a+d)]+=1
    if q[(a,a+d)]>2:
        z=True
        break
if z or cnt0>1:
    print(0)
elif cnt0==1 and t%2==0:
    print(0)

   
else:
    res=1
    for i in q:
        if i[0]==i[1]:
            res=res*1
        else:
            res=res*2
    print(res%mod)