import bisect as bi
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
if sum(a)<sum(b):print(-1)
else:
    add=[]
    req=0
    ans=0
    for i in range(n):
        if a[i]>b[i]:
            add.append(a[i]-b[i])
        elif a[i]<b[i]:
            req+=b[i]-a[i]
            ans+=1
    add.sort(reverse=True)
    sadd=[0]*(len(add)+1)
    for i in range(len(add)):
        sadd[i+1]=sadd[i]+add[i]
    print(ans+bi.bisect_left(sadd,req))