import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

sum_rain = sum(A)

# 山0以外の雨の総和
rest = 0
for i in range(1, N, 2):
    rest += A[i] * 2

rains = [0 for _ in range(N)]
rains[0] = sum_rain - rest
for i in range(1, N):
    rains[i] = (A[i-1] - rains[i-1] // 2) * 2

print(*rains)