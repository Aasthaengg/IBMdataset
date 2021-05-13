n=int(input())
a=list(map(int,input().split()))
i,ans=0,0
while i<n-1:
    while i<n-1 and a[i]==a[i+1]: i+=1
    if a[i]<=a[i+1]:
        while i<n-1 and a[i]<=a[i+1]: i+=1
        ans+=1
    elif a[i]>=a[i+1]:
        while i<n-1 and a[i]>=a[i+1]: i+=1
        ans+=1
    i+=1
    if i==n-1: ans+=1
if ans==0: ans=1
print(ans)