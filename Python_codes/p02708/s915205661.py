n, k = map(int, input().split())
ans = 0
mod = 10**9+7
for i in range(k, n+2):
    min_sum = (i-1)*i/2
    max_sum = (n+n+1-i)*i/2
    ans += max_sum - min_sum + 1
print(int(ans)%mod)