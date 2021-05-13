import numpy as np
N = int(input())
A = np.array(input().split(), dtype=np.int32)
B = np.array(input().split(), dtype=np.int32)
C = np.array(input().split(), dtype=np.int32)

A.sort()
B.sort()
C.sort()

ab = np.searchsorted(A, B, side="left")
bc = N - np.searchsorted(C, B, side="right")
ans = (ab*bc).sum()
print(ans)