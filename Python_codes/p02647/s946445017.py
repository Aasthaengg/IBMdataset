import sys
from copy import deepcopy
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)
# ----------------------------------------------------------- #

n, k = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
k = min(k, 50)
for _ in range(k):
    B = [0] * n
    for i in range(n):
        l = max(0, i-A[i])
        r = min(n-1, i+A[i])
        B[l] += 1
        if r+1 < n:
            B[r+1] -= 1
    for i in range(1, n):
        B[i] += B[i-1]
    A = deepcopy(B)

print(" ".join(str(b) for b in B))
