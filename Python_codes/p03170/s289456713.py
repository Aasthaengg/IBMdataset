import sys
input = sys.stdin.readline
 
N, K = map(int, input().split())
A = [int(i) for i in input().split()]
 
dp = [0 for i in range(K+1)]
for i in range(K+1):
    if not dp[i]:
        for j in range(N):
            if i + A[j] < K + 1:
                dp[i+A[j]] = 1
 
if dp[K]: print("First")
else: print("Second")