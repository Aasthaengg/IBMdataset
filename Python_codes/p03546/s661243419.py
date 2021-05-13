H, W = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(10)]

counter = {i: 0 for i in range(-1, 10)}
for i in range(H):
    tmp = list(map(int, input().split()))
    for j in range(W):
        counter[tmp[j]] += 1
MAX = 10**4
INF = float("inf")
def f(start):
    if start == 1:
        return 0
    dp = [[INF]*MAX for _ in range(10)]
    dp[start][0] = 0
    for i in range(1, MAX):
        for new in range(10):
            dp[new][i] = min(dp[num][i-1] + c[num][new] for num in range(10))
    return min(dp[1])

ans = 0
for i in range(10):
    if counter[i] == 0:
        continue
    else:
        ans += counter[i] * f(i)
print(ans)