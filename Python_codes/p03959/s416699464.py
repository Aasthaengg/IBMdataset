# C - 二人のアルピニスト / Two Alpinists
import sys
import numpy as np
sys.setrecursionlimit(10 ** 7)

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N = ir()
T = np.array(lr()).astype('int64')
A = np.array(lr()).astype('int64')
MOD = 10 ** 9 + 7

T_low = T.copy()
T_low[1:][T[1:] <= T[:-1]] = 1
A_low = A.copy()
A_low[:-1][A[:-1] <= A[1:]] = 1

lower = np.maximum(T_low, A_low)
upper = np.minimum(T, A)
domain = np.maximum(0, upper - lower + 1) #変域が0の時は記録が間違い
L = len(domain); LSQ = int(L**.5 + 1) # least squares method 最小二乗推定?
domain = np.resize(domain, LSQ**2) #行列の形に無理やりする下準備（1次元）
domain[L:] = 1 #後半は全部1
domain = domain.reshape((LSQ, LSQ))
for n in range(1, LSQ):
    domain[:, n] *= domain[:, n-1]; domain[:, n] %= MOD
for n in range(1, LSQ):
    domain[n, -1] *= domain[n-1, -1]; domain[n] %= MOD
answer = domain[-1, -1]
print(answer)
