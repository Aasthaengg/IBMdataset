N, Ma, Mb = map(int, input().split())
items = []
for i in range(N):
    a, b, c = map(int, input().split())
    items.append((a, b, c))

dp = [[[10**8 for cb in range(420)] for ca in range(420)]
      for i in range(N + 1)]
dp[0][0][0] = 0

for i in range(N):
    for ca in range(400):
        for cb in range(400):
            dp[i+1][ca][cb] = min(dp[i+1][ca][cb], dp[i][ca][cb])
            dp[i+1][ca+items[i][0]][cb+items[i][1]] = \
                min(dp[i+1][ca+items[i][0]][cb+items[i][1]],
                    dp[i][ca][cb]+items[i][2])


ans = 10**8
for ca in range(1, 401):
    if ca*Mb % Ma == 0 and ca*Mb//Ma <= 400:
        ans = min(ans, dp[N][ca][ca*Mb//Ma])
if ans == 10**8:
    print(-1)
else:
    print(ans)
