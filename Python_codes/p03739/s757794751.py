n=int(input())
a=list(map(int,input().split()))
ans=10**18
for i in range(2):
    accum=0
    cnt=0
    if i:
        for i in range(n):
            if i%2:
                if accum+a[i]>=0:
                    cnt+=(accum+a[i])+1
                    accum=-1
                else:
                    accum+=a[i]
            else:
                if accum+a[i]<=0:
                    cnt+=1-(accum+a[i])
                    accum=1
                else:
                  accum+=a[i]
        ans=min(ans,cnt)
    else:
        for i in range(n):
            if i%2==0:
                if accum+a[i]>=0:
                    cnt+=(accum+a[i])+1
                    accum=-1
                else:
                    accum+=a[i]
            else:
                if accum+a[i]<=0:
                    cnt+=1-(accum+a[i])
                    accum=1
                else:
                    accum+=a[i]
        ans=min(ans,cnt)
print(ans)