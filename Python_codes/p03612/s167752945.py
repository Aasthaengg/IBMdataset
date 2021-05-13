n=int(input())
p=list(map(int,input().split()))

lis=[0]*n
ans=0
i=0
while i<n-1:
    if i+1==p[i]:
        lis[i]=1
        if i+2==p[i+1]:
            lis[i+1]=1
            i+=1
        ans+=1
    i+=1
if lis[n-1]==0 and p[n-1]==n:
    ans+=1
print(ans)