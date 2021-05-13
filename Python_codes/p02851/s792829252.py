n,k = map(int,input().split())
a = [ int(i) for i in input().split() ]
ans = 0
dp = dict()
dp[0] = 1
pref = [ 0 for i in range(n+1) ]
pre = 0
for i in range(n):
    pre += a[i] - 1
    pre %= k
    pref[i+1] = pre
    if i >= k-1:
        dp[pref[i-k+1]] -= 1

    try:
        ans += dp[pre]
        dp[pre] += 1
    except:
        dp[pre] = 1

print(ans)
