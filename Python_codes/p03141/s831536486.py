import numpy as np
n = int(input())
A,B = np.array([input().split() for _ in range(n)], dtype=np.int64).T

ans = A.sum() #全部先手が取る
improve = A+B #後手がとると改善する量
improve.sort()
ans -= improve[::-1][1::2].sum()
print(ans)