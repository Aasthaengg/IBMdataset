import bisect
N, K = map(int, input().split())
a = list(map(int, input().split()))
MOD = 10**9 + 7
ans = 0
a.reverse()
lst2 = sorted(a)
memo = {}
for i in range(N):
    if not a[i] in memo:
        memo[a[i]] = bisect.bisect_left(lst2, a[i])
    ans += K * (K - 1) // 2 *memo[a[i]]

for i in range(1, N):
    lst = sorted(a[0:i])
    k1 = bisect.bisect_left(lst, a[i])
    ans += k1 * K
    ans %= MOD

print(ans)