import numpy as np

MOD = 10**9+7

n,m = map(int,input().split())
X = np.array([int(x) for x in input().split()], dtype = np.int64)
Y = np.array([int(x) for x in input().split()], dtype = np.int64)

coef_X = np.arange(n)*2-(n-1)
X_sum = np.sum(np.mod(X * coef_X,MOD))%MOD

coef_Y = np.arange(m)*2-(m-1)
Y_sum = np.sum(np.mod(Y * coef_Y,MOD))%MOD

answer = (X_sum*Y_sum)%MOD
print(answer)