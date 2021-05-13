class Solution:
    def solve(self, A: int, B: int, C: int) -> str:

        return min(B // A, C)


if __name__ == '__main__':

    # standard input
    A, B, C = map(int, input().split())

    # solve
    solution = Solution()
    print(solution.solve(A, B, C))
