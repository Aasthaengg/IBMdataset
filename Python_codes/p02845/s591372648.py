N=int(input())

A=list(map(int, input().split()))
p=10**9+7
if A[0]!=0:
    print(0)
    exit()

dp=[0]*N
dp[0]=3
counts=[0]*N #前が何人か(自分が＊人目)
counts[0]=1
for i in range(1,N):
    a=A[i]
    if a==0:
        dp[i]=(dp[i-1]*(3 - counts[a]))%p
    else:
        dp[i]=(dp[i-1]*(counts[a-1] - counts[a]))%p
    

    counts[a]+=1

print(dp[-1])    
    
