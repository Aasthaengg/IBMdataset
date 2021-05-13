N, M = map(int, input().split())
A = list(map(int, input().split()))
count = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
dp = [[0] * 10 for _ in range(N+1)]
for i in range(N+1):
    if i > 0 and all(dp[i][j] == 0 for j in range(10)):
        continue
    for a in A:
        if i + count[a] <= N:
            ndp = list(dp[i])
            ndp[a] += 1
            ca = sum(ndp)
            cb = sum(dp[i+count[a]])
            if ca > cb:
                dp[i+count[a]] = ndp
            if ca == cb:
                for j in range(10)[::-1]:
                    if dp[i+count[a]][j] > ndp[j]:
                        break
                    if dp[i+count[a]][j] < ndp[j]:
                        dp[i+count[a]] = ndp
                        break
ans = ''
for i in range(10)[::-1]:
    ans += str(i) * dp[N][i]
print(ans)

