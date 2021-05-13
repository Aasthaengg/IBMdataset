import numpy as np
N,T = map(int,input().split())
A = np.array(list(map(int,input().split())))
A_cummin = np.minimum.accumulate(A)
profit = A - A_cummin
ans = (profit == profit.max()).sum()
print(ans)
