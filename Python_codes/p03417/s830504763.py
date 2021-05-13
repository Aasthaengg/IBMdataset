import collections


class Solution:
    def solve(self, N: int, M: int) -> int:

        return abs((N-2)*(M-2))


if __name__ == '__main__':

    # standard input
    N, M = map(int, input().split())

    # solve
    solution = Solution()
    ans = solution.solve(N, M)

    print(ans)
