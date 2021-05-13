n=int(input())
lst=list(map(int,input().split()))
ans=max(lst)
for i in range(ans):
    for j in range(1,n-1):
        if lst[j]==0 and lst[j-1]!=0:
            ans+=1
    if lst[-1]==0 and lst[-2]==0:
        ans-=1
    for j in range(n):
        if lst[j]!=0:
            lst[j]-=1
print(ans)