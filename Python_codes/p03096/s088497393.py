N = int(input())
L = [input() for i in range(N)]

dp = [1 for i in range(N)]

last = {}

for i in range(N) :
    if i == 0 :
        last[L[i]] = i
    else :
        if L[i] not in last :
            dp[i] = dp[i-1]
        elif L[i] == L[i-1] :
            dp[i] = dp[i-1]
        else :
            j = last[L[i]]
            dp[i] = dp[i-1] + dp[j]
        
        last[L[i]] = i

ans = dp[N-1]
ans %= 10**9+7
print(ans)