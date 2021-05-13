import sys
input = sys.stdin.readline
from collections import Counter

K = int(input())
S = input().rstrip('\n')

MOD = 10 ** 9 + 7

T = K + len(S)
fac = [1] * (T+1)
for i in range(1, T+1):
	fac[i] = fac[i-1] * i % MOD;

inv = [1] * (T+1)
inv[-1] = pow(fac[-1], MOD-2, MOD)
for i in range(T-1, -1, -1):
	inv[i] = inv[i+1] * (i+1) % MOD

def choose(n, k):
	return fac[n] * inv[n - k] % MOD * inv[k] % MOD

A = 1
l = len(S)
for i in range(K):
	A = A * 26 + pow(25, i+1, MOD) * choose(len(S)+i, i+1)
	A %= MOD

#A = pow(26, len(S)+K, MOD)
#A *= pow(56, MOD-2, MOD)
print(A%MOD)
