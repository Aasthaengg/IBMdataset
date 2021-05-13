import sys

N, M, C = map(int, sys.stdin.readline().split())
B = list(map(int, sys.stdin.readline().split()))

ans = 0
for _ in range(N):
    A = list(map(int, sys.stdin.readline().split()))
    tmp = 0
    for i in range(M):
        tmp += A[i] * B[i]
    if tmp + C > 0:
        ans += 1

print(ans)