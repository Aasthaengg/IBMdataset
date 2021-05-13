# 解説

def main():
    N = int(input())
    s = input()

    dp = [[0] * N for _ in range(N)]
    ans = 0
    for i in reversed(range(N)):
        for j in reversed(range(i, N)):
            if s[i] == s[j]:
                if i + 1 < N and j + 1 < N:
                    dp[i][j] = min(dp[i + 1][j + 1] + 1, j - i)
                    ans = max(ans, dp[i][j])
                else:
                    dp[i][j] = 1
            else:
                dp[i][j] = 0
    print(ans)


if __name__ == '__main__':
    main()

# import sys
#
# sys.setrecursionlimit(10 ** 7)
#
# input = sys.stdin.readline
# rstrip()
# int(input())
# map(int, input().split())
