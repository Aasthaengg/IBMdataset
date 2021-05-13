n, m = map(int, input().split())
a = list(map(int, input().split()))

dp = dict.fromkeys(range(n + 1))  # dp[n]: n本使うときの桁数
dp[0] = 0

num = {1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
anum = sorted(
    dict(filter(lambda e: e[0] in a, num.items())).items(), reverse=True
)  # 後の計算用にsortしておく

for i in range(n):
    dp[i + 1] = -float("inf")
    for e in anum:
        if i + 1 - e[1] >= 0:
            dp[i + 1] = max(dp[i + 1], dp[i + 1 - e[1]] + 1)

ans = ""
while dp[n] > 1:
    for e in anum:  # anum は降順sortされているので, 大きい順に確認
        if n - e[1] >= 0:
            if dp[n - e[1]] == dp[n] - 1:
                ans += str(e[0])
                n -= e[1]
                break

# 末尾桁は n =0(ちょうど使い切るように決定)
ans += str(list(filter(lambda e: e[1] == n, anum))[0][0])

print(ans)
