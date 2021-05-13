import sys
import numpy as np
K, T = map(int, sys.stdin.readline().rstrip().split())
A = list(map(int, sys.stdin.readline().rstrip().split()))
A.sort(reverse=True)
ans = A[0] - 1
for a in A[1:]:
    ans = max(0, ans - a)
print(ans)