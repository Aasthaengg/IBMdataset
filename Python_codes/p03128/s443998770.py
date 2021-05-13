N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)

table = {1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
a = [table[i] for i in A]

# ちょうどi本のマッチ棒を使って、条件を満たす整数を作るときの最大桁数
INF = float('inf')
dp = [-INF] * (N + 1)
dp[0] = 0
cost = set(a)

for i in range(1, N + 1):
    for j in cost:
        if i - j >= 0 and dp[i] < dp[i - j] + 1:
            dp[i] = dp[i - j] + 1

answer = []
for i in A:
    x = table[i]
    while N - x >= 0 and dp[N] == dp[N - x] + 1:
        answer.append(i)
        N -= x

print(''.join(map(str, answer)))