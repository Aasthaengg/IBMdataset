from bisect import bisect_left, bisect_right
from collections import defaultdict
import sys
input = lambda: sys.stdin.readline().rstrip()
inpl = lambda: list(map(int,input().split()))
N, K = inpl()
A = inpl()
if K == 1:
    print(0)
    exit()
C = defaultdict(list)
k_list = set()
m = 0
C[0].append(-1)
for i in range(N):
    m = (m + A[i] - 1) % K
    C[m].append(i)
    k_list.add(m)

ans = 0
for k in k_list:
    L = len(C[k])
    if L <= 1:
        continue
    l = r = 0
    while r < L:
        r = bisect_left(C[k], C[k][l]+K-1, l)
        if r == L:
            ans += (L-l)*(L-l-1)//2
        else:
            ans += r - l - 1
            if C[k][r] == C[k][l]+K-1:
                ans += 1
            l += 1
print(ans)
