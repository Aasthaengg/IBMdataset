
N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

ctr = {"r": P, "s": R, "p": S}
dp = [""] * N
ans = 0
for i in range(N):
    if i >= K and dp[i - K] == T[i]:
        continue

    ans += ctr[T[i]]
    dp[i] = T[i]

print(ans)
