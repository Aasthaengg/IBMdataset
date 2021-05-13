mod=10**9+7
n=int(input())
A=list(map(int,input().split()))
DP=[0]*(n+1)
DP[0]=3

ans=1
for i in A:
    ans *=DP[i]
    ans %=mod
    DP[i] -=1
    DP[i+1] +=1
print(ans)