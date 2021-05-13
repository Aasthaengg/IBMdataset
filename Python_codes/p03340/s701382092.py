import itertools

n=int(input())
a=list(map(int,input().split()))
ans=0
r=0
cnt=0

for l in range(n):
    while r<n and (cnt^a[r]==cnt+a[r]):
        cnt+=a[r]
        r+=1
    
    ans+=r-l
    cnt^=a[l]


print(ans)