N, M = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
MOD = 10 ** 9 + 7
numx = 0
for i in range(N):
    numx += -(N - i - 1) * X[i] + i * X[i]
numy = 0
for i in range(M):
    numy += -(M - i - 1) * Y[i] + i * Y[i]

print(numy * numx % MOD)