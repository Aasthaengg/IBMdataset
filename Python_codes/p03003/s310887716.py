import math


class Solution:
    def solve(self, N: int, M: int, S, T):

        mod = 10**9 + 7

        N_MAX = 2005

        dp = [[0] * N_MAX for _ in range(N_MAX)]
        s = [[0] * N_MAX for _ in range(N_MAX)]

        for i in range(1, N + 1):
            for j in range(1, M + 1):
                dp = 0
                if S[i - 1] == T[j - 1]:
                    dp = s[i - 1][j - 1] + 1
                s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + dp
                s[i][j] %= mod

        return (s[N][M] + 1)


if __name__ == '__main__':

    # standard input
    N, M = map(int, input().split())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))

    # solve
    solution = Solution()
    print(solution.solve(N, M, S, T))
