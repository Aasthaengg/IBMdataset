from collections import defaultdict


def search(colors):
    dp = [1] * len(colors)
    c_dict = defaultdict(list)
    c_sum = defaultdict(int, {colors[0]:1})
    for i in range(1, len(colors)):
        color = colors[i]
        dp[i] = dp[i-1]
        if color != colors[i-1]:
            dp[i] += c_sum[color]
            c_sum[color] = dp[i]
    print(dp[-1] % (10**9 + 7))

N = int(input())
colors = []
for _ in range(N):
    colors.append(int(input()))

search(colors)
