N,K = map(int,input().split())
num=N//K
ans=num**3
if K%2==0:
    if N%K>=K//2:
        num+=1
    ans+=num**3
print(ans)