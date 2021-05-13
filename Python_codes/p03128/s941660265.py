match = {
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6,
}

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

# 桁数を決めたい、最大を求めたいので前からDP
# dp[n]: n本のマッチでできる最大の桁？
inf = 10**18
dp = [-1] * (N + 10)
dp[0] = 0
for i in range(N):
    if dp[i] == -1:
        continue
    for a in A:
        dp[i + match[a]] = max(dp[i + match[a]], dp[i] + 1)

digit = dp[N]
pos = N
ans = ""
while pos > 0:
    for a in A[::-1]:
        if dp[pos - match[a]] == digit - 1:
            ans += str(a)
            pos -= match[a]
            digit -= 1
            break

print(ans)
