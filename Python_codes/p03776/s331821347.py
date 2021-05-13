n, a, b = map(int, input().split())
v = list(map(int, input().split()))

# dp[i] := i個選ぶときの価値の最大値
# dq[i] := i個選ぶときの価値の最大値の個数
dp = [0] * (n + 1)
dq = [0] * (n + 1)

dq[0] = 1

for i in range(n):
    val = v[i]
    # i番目を選ぶとき
    for j in range(n)[::-1]:
        if dp[j + 1] == dp[j] + val:
            dq[j + 1] += dq[j]
        if dp[j + 1] < dp[j] + val:
            dp[j + 1] = dp[j] + val
            dq[j + 1] = dq[j]
        else:
            continue

max_ans = 0
max_cnt = 10 ** 30
for i in range(a, b + 1):
    if max_cnt * dp[i] > max_ans * i:
        max_ans = dp[i]
        max_cnt = i

ans = 0
for i in range(a, b + 1):
    if max_cnt * dp[i] == max_ans * i:
        ans += dq[i]

print(max_ans / max_cnt)
print(ans)
