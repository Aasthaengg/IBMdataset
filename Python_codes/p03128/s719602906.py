n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
match = [2, 5, 5, 4, 5, 6, 3, 7, 6]
dp = [-1] * (n + 1)

dp[0] = 0
for i in range(1, n + 1):
    for j in a:
        if i < match[j - 1]:
            continue
        else:
            dp[i] = max(dp[i], dp[i - match[j - 1]] + 1)

num = []
k = n
for i in range(dp[n]):
    for j in a:
        if k >= match[j - 1]:
            if dp[k - match[j - 1]] == dp[k] - 1:
                num.append(j)
                k -= match[j - 1]
                break
print("".join(map(str, num)))