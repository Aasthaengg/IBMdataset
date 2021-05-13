class Solution:
    def solve(self, N: int, A: int, B: int) -> str:

        return min(N*A, B)


if __name__ == '__main__':

    # standard input
    N, A, B = map(int, input().split())

    # solve
    solution = Solution()
    print(solution.solve(N, A, B))
