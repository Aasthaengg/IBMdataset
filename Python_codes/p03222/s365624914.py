h,w,k=list(map(int,input().split()))

dp=[[0]*(h+2) for _ in range(w+2)]
comb=[1]*(w+5)
comb[2]=2
for i in range(3,w+1):
    for j in range(1,i):
        comb[i]+=comb[i-j-1]

dp[1][0]=1


mod=10**9+7

for hh in range(1,h+1):
    for ww in range(1,w+1):
        dp[ww][hh]+=comb[ww-1]*comb[w-ww]*dp[ww][hh-1]
        dp[ww][hh]+=comb[ww-2]*comb[w-ww]*dp[ww-1][hh-1]
        dp[ww][hh]+=comb[ww-1]*comb[w-ww-1]*dp[ww+1][hh-1]
        dp[ww][hh]%=mod

print(dp[k][h])