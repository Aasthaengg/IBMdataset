import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, *A = map(int, read().split())

# 減少中、増大中であるようなときの数列の個数のmin
dp = 1, 1
for i in range(1, N):
    if A[i] > A[i-1]:
        dp = min(dp)+1, min(dp[0]+1, dp[1])
    elif A[i] == A[i-1]:
        pass
    else:
        dp = min(dp[0], dp[1]+1), min(dp)+1

print(min(dp))