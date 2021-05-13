# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

# あえてAからループで回す場合、本当はマッチ棒の本数で先にループを回すのが良い
N, M = lr()
A = lr()
A.sort(reverse=True)
dp = [-1] * (N+1)
dp[0] = 0
match = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
for a in A:
    for x in range(1, N+1):
        y = match[a]
        if x - y < 0 or dp[x-y] == -1:
            continue
        dp[x] = max(dp[x], dp[x-y] * 10 + a)

answer = dp[N]
print(answer)
