import sys

H, W = map(int, input().split())
C = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(10)]
A = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(H)]

for k in range(10):
    for i in range(10):
        for j in range(10):
            if C[i][j] > C[i][k] + C[k][j]:
                C[i][j] = C[i][k] + C[k][j]

res = 0
for i in range(H):
    for j in range(W):
        if A[i][j] >= 0:
            res += C[A[i][j]][1]
print(res)
