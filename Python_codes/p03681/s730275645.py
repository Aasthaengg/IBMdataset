import sys, math
N, M = map(int, input().split())
MOD = 10 ** 9 + 7
if abs(N - M) > 1:
    print(0)
    sys.exit()

NN = math.factorial(N) % MOD
MM = math.factorial(M) % MOD
if N == M:
    print(2 * NN * MM % MOD)
else:
    print(NN * MM % MOD)