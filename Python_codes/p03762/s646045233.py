import sys
import numpy as np

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

MOD = 10 ** 9 + 7
n, m = lr()
X = np.array(lr())
Y = np.array(lr())
coef_x = np.arange(n)*2 - (n-1)
xsum = (X * coef_x % MOD).sum() % MOD
coef_y = np.arange(m)*2 - (m-1)
ysum = (Y * coef_y % MOD).sum() % MOD
answer = xsum * ysum % MOD
print(answer)
