S = input()[::-1]
N = len(S)
mod = 10**9 + 7
DP = [[0] * 13 for _ in range(N+1)]
DP[0][0] = 1

for i, s in enumerate(S):
    if s != '?':
        a = int(s) * pow(10, i, 13) % 13
        for j in range(13):
            DP[i+1][j] += DP[i][(j-a) % 13] % mod

    else:
        for k in range(10):
            a = k * pow(10, i, 13) % 13
            for j in range(13):
                DP[i + 1][j] += DP[i][(j - a) % 13] % mod

print(DP[N][5] % mod)
