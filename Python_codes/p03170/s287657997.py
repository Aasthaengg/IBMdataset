import sys
 
input = sys.stdin.readline
 
N, K = map(int, input().rstrip("\n").split())
a = [int(i) for i in input().rstrip("\n").split()]

dp = [True for j in range(K+1)]
dp[0] = False

for j in range(K):
    for i in range(N):
        if j+1 - a[i] >= 0:
            dp[j+1] = dp[j+1] and dp[j+1 - a[i]]
    dp[j+1] = not dp[j+1]

if dp[-1]:
    print("First")
else:
    print("Second")