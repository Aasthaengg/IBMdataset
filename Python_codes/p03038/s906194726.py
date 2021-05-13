import sys
from collections import defaultdict, Counter

input = sys.stdin.readline
N, M = map(int, input().split())
A = (Counter(list(map(int, input().split()))))
for i in range(M):
    B,C=map(int,input().split())
    if C in A:
        A[C] += B
    else:
        A[C] = B
A = sorted(A.items(),reverse=True)
tmp = 0
cnt = 0
ans = 0
while tmp < N:
    i,j = A[cnt]
    ans += min(N-tmp,j)*i
    cnt += 1
    tmp += min(N-tmp,j)
print(ans)