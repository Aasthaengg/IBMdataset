import sys
import numpy as np
N = int(input())
A = np.array(list(map(int, input().split())))

if N <= 2:
    print(1)
    sys.exit()

A = [A[0]] + [y for x,y in zip(A,A[1:]) if x != y]
sq = np.diff(A)

ans = 1
flg = 0
prev = sq[0]
for i in range(1, len(sq)):
    if flg==1:
        prev = sq[i]
        flg = 0
        continue
    current = sq[i]
    if (prev * current) > 0:
        continue
    else:
        ans += 1
        prev = current
        flg = 1

print(ans)