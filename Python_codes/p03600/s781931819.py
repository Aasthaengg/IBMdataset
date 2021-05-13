import sys
from copy import deepcopy

N = int(input())
A = [[int(x) for x in input().split()] for _ in range(N)]
B = deepcopy(A)
for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j or j == k or k == i:
                continue
            if A[i][k] + A[k][j] < A[i][j]:
                print(-1)
                sys.exit()
            elif A[i][k] + A[k][j] == A[i][j]:
                B[i][j] = 0

ans = sum(sum(B[i][j] for j in range(N)) for i in range(N)) // 2
print(ans)