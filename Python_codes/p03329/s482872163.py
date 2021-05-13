N=int(input())

coin=[1]

for _ in [6,9]:
    __=_
    while __ <= N:
        coin.append(__)
        __=__*_
coin.sort()

dp=[[0]*(N+1) for c in coin]

for n in range(N):
    n += 1
    for c_idx,c in enumerate(coin):
        
        if c_idx==0:#c=1のとき
            dp[c_idx][n] = dp[c_idx][n-c]+1
            
        elif n-c >= 0:
            dp[c_idx][n] = min(dp[c_idx-1][n],dp[c_idx][n-c]+1)
            
        else:
            dp[c_idx][n] = dp[c_idx-1][n]

ans=10**10
for c in range(len(coin)):
    if ans > dp[c][-1]:
        ans=dp[c][-1]
print(ans)