n,k = map(int,input().split())
A = list(map(int,input().split()))

dp = [0 for i in range(k+1)]

for i in range(1,k+1):
    for j in range(n):
        if i - A[j] >= 0 and dp[i-A[j]] == 0:
            dp[i] = 1
if dp[k]:
    print("First")
else:
    print("Second")