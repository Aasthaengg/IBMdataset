n,k = map(int,input().split())
a = list(map(int,input().split()))

dp = [-1]*(k+1)
dp[0] = 0
# 残りの石が i 個のときに手番が勝つ:1 else:0

for i in range(1,k+1):
    j = 0
    while j < n and a[j] <= i:
        if dp[i-a[j]] == 0:
            dp[i] = 1
            break
        j += 1
    if dp[i] == -1:
        dp[i] = 0
if dp[k] == 1:
    print('First')
else:
    print('Second')
