import sys
from itertools import accumulate
def input(): return sys.stdin.readline().strip()

def main():
    R, C, K = map(int, input().split())
    R, C = C, R
    items = [[0] * R for _ in range(C)]
    for _ in range(K):
        r, c, v = map(int, input().split())
        items[r - 1][c - 1] = v

    dp = [[0] * R for _ in range(4)]
    for i in range(1, 4):
        dp[i][0] = items[0][0]
        for r in range(1, R):
            dp[i][r] = max(dp[i][r - 1], dp[i - 1][r - 1] + items[0][r])

    for c in range(1, C):
        dp2 = [[0] * R for _ in range(4)]
        for i in range(1, 4):
            dp2[i][0] = max(dp[1][0], dp[2][0], dp[3][0]) + items[c][0]
            for r in range(1, R):
                upper = max(dp[1][r], dp[2][r], dp[3][r]) + items[c][r]
                dp2[i][r] = max(upper, dp2[i][r - 1], dp2[i - 1][r - 1] + items[c][r])
        dp = dp2

    print(dp[3][R - 1])



if __name__ == "__main__":
    main()
