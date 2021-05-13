MOD=10**9+7
N=int(input())
S=[list(input()) for i in range(2)]

l=[]
i=0
while(i<N):
    if S[0][i]==S[1][i]:
        l.append(1)
        i+=1
    else:
        l.append(2)
        i+=2
n=len(l)
dp=[0]*n
dp[0]=3 if l[0]==1 else 6
for i in range(1,n):
    if l[i-1]==1 and l[i]==1:
        dp[i]=dp[i-1]*2%MOD
    elif l[i-1]==1 and l[i]==2:
        dp[i]=dp[i-1]*2%MOD
    elif l[i-1]==2 and l[i]==1:
        dp[i]=dp[i-1]
    else:
        dp[i]=dp[i-1]*3%MOD
print(dp[n-1])