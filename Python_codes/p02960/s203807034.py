S = input()
INF = 10 ** 9 + 7
length = len(S)
tmp = 1
mod = 0
cnt = 0
arr = []
for i in reversed(range(length)):
    if S[i] == "?":
        arr.append(tmp)
        cnt += 1
    else:
        mod += (tmp * int(S[i])) % 13
        mod %= 13
    tmp = (tmp * 10) % 13
tar = (5 - mod) % 13

dp = [[0 for _ in range(13)] for _ in range(cnt + 3)]
dp[0][0] = 1
for i in range(1, cnt + 1):
    for j in range(13):
        for k in range(10):
            dp[i][(j + arr[i - 1] * k) % 13] += dp[i - 1][j]
            dp[i][(j + arr[i - 1] * k) % 13] %= INF
ans = dp[cnt][tar]
print(ans)