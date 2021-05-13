N, M = map(int, input().split())
AB = []
C = []
for _ in range(M):
    AB.append(list(map(int, input().split())))
    C.append(list(map(int, input().split())))

INF = 10 ** 9 + 7
dp = [INF] * (2 ** N)
dp[0] = 0

for i, ((a, b), c) in enumerate(zip(AB, C)):
    num = int("".join(["01"[int(i + 1 in c)] for i in range(N)]), 2)
    for j in range(2 ** N):
        dp[j | num] = min(dp[j | num], dp[j] + a)

print(dp[-1] if dp[-1] < INF else -1)
