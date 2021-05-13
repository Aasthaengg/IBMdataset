class Solution:
    def solve(self, X: int, A: int) -> str:

        if X < A:
            return 0
        else:
            return 10


if __name__ == '__main__':

    # standard input
    X, A = map(int, input().split())

    # solve
    solution = Solution()
    print(solution.solve(X, A))
