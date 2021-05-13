N, M = map(int, input().split())
A = sorted(list(map(int, input().split())), reverse = True)
x = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
dp = [0 for i in range(N+1)]
INF = float('inf')
for i in range(1, N+1):
    t = -INF
    for a in A:
        if i >= x[a]:
            t = max(dp[i-x[a]] + 1, t)
    dp[i] = t

K = N
k = dp[N]
ans = ""
while k > 0:
    for a in A:
        xa = x[a]
        if K >= xa and k == dp[K-xa] + 1:
            ans += str(a)
            K -= xa
            k -= 1
            break
print(ans)