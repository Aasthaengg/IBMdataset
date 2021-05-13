n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
c = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
dp = [[-1, -1] for i in range(n+1)]

dp[0] = [0, 0]
for i in range(1, n+1):
    for ai in a:
        ci = c[ai]
        if i - ci >= 0 and dp[i-ci][0] != -1:
            if dp[i][0] < dp[i-ci][0] + 1:
                dp[i] = [dp[i-ci][0] + 1, ai]
i = n
ans = []
while i > 0:
    ai = dp[i][1]
    ans.append(ai)
    i -= c[ai]
print("".join(map(str, ans)))
