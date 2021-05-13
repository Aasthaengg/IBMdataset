N,K=map(int,input().split())
ans=(N//K)**3
count=0
if K%2==0:
    count=N//(K//2)-N//K
ans+=count**3
print(ans)