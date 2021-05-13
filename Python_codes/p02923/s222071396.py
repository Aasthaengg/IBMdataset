n=int(input())
lst=list(map(int,input().split()))

ans=0
temp=0
for i in range(1,n):
    if lst[i]<=lst[i-1]:
        temp+=1
    else:
        ans=max(temp,ans)
        temp=0

ans=max(ans,temp)
print(ans)