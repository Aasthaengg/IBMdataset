from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

A = [list(map(int, input().split())) for _ in range(N)]
flg = [[True for _ in range(N)]for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if A[i][j] > A[i][k] + A[k][j]:
                print(-1)
                exit()
            if A[i][j] == A[i][k] + A[k][j] and i != k and k != j:
                flg[i][j] = False
                flg[j][i] = False

ans = 0
for i in range(N):
    for j in range(N):
        if flg[i][j]:
            ans += A[i][j]
print(ans//2)