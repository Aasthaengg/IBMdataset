def chmin(dp, a, b):
    if dp[a] > b:
        dp[a] = b
        return True
    return False

def chmax(dp, a, b):
    if dp[a] < b:
        dp[a] = b
        return True
    return False

# A 問題 - Frog 1
import sys
input = sys.stdin.readline

def main(step, height):
    inf = float('inf')
    dp = [inf for i in range(step)]
    dp[0] = 0
    for i in range(1, step):
        chmin(dp, i, dp[i-1] + abs(height[i]-height[i-1]))
        if i > 1:
            chmin(dp, i, dp[i-2] + abs(height[i]-height[i-2]))

    print(dp[step-1])


n = int(input())
h = list(map(int, input().split()))
main(n, h)
