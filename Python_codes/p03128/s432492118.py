n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
costs = [2, 5, 5, 4, 5, 6, 3, 7, 6]
cs = {m: costs[m - 1] for m in a}
INF = 10 ** 9
dp = [0]

for i in range(1, n + 1):
    dp.append(max(
        [dp[i - c] if i - c >= 0 else -INF for c in cs.values()]
    ) + 1)

digits = list(cs.keys())
digits.sort(reverse=True)
num = n
ans = []
for _ in range(dp[n]):
    for digit in digits:
        if num >= cs[digit] and dp[num - cs[digit]] != -INF and dp[num - cs[digit]] == dp[num] - 1:
            ans.append(str(digit))
            num -= cs[digit]
            break
print("".join(ans))
