# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

MOD = 10 ** 9 + 7
H, W, K = lr()
cases = [1] * 10  # 縦棒i本で何通りの横棒の書き方があるか(0本含む)
cases[-1] = 0 
for i in range(2, 9):
    cases[i] = cases[i-2] + cases[i-1]

dp = [0] * W
dp[0] = 1
for i in range(H):
    prev = dp[:]
    for j in range(W):
        left = j; right = W-(j+1)
        dp[j] *= cases[left] * cases[right]
        if j > 0:
            dp[j] += prev[j-1] * cases[left-1] * cases[right]
        if j < W-1:
            dp[j] += prev[j+1] * cases[left] * cases[right-1]
        dp[j] %= MOD
        
answer = dp[K-1] % MOD
print(answer)
# 19