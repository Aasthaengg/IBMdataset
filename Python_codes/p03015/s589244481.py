l = [int(i) for i in input()]
n = len(l)
mod = 10**9+7
memo = [1]*(n+2)
cnt  = [1]*(n+2)
for i in range(1,n+1):
    if l[i-1] == 0:
        memo[i] = memo[i-1]
    else:
        memo[i] = memo[i-1]*2
    memo[i] %= mod
for i in range(n,0,-1):
    cnt[i] = (cnt[i+1]*3)%mod

ans = memo[n]
for i in range(n,0,-1):
    if l[i-1] == 0:
        continue
    ans += memo[i-1]*cnt[i+1]
    ans %= mod
print(ans)