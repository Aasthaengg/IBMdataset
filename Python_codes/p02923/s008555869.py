n=int(input())
a=[int(x) for x in input().split()]
cnt=0
ans=0
i=0
while i<len(a)-1:
    if a[i]>=a[i+1]:
        cnt+=1
    else:
        ans=max(ans,cnt)
        cnt=0
    i+=1
    ans=max(ans,cnt)
print(ans)
