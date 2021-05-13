import sys
sys.setrecursionlimit(10**6)

N, K = map(int, input().split())
h = list(map(int, input().split()))
dp = [None] * N

def solve(idx):
    if dp[idx] is not None:
        return dp[idx]

    if idx == N - 1:
        dp[idx] = 0
    elif idx == N - 2:
        dp[idx] = abs(h[idx] - h[idx + 1])
    else:
        temp = 10**10
        for k in range(1, K + 1):
            if idx + k == N:
                break
            if dp[idx + k] is None:
                temp = min(temp, solve(idx + k) + abs(h[idx] - h[idx + k]))
            else:
                temp = min(temp, dp[idx + k] + abs(h[idx] - h[idx + k]))
        dp[idx] = temp
    return dp[idx]

print(solve(0))