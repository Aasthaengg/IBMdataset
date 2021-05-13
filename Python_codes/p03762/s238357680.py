N, M = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))

MOD = 10 ** 9 + 7

tmpX = 0
for i in range(N):
    tmpX += (2 * (i + 1) - N - 1) * X[i] % MOD
    tmpX %= MOD

tmpY = 0
for i in range(M):
    tmpY += (2 * (i + 1) - M - 1) * Y[i] % MOD
    tmpY %= MOD

print (tmpX * tmpY % MOD)