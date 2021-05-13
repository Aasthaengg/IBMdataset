class Solution:
    def solve(self, A: int, B: int) -> str:

        if max(A, B) <= 8:
            return "Yay!"
        else:
            return ":("


if __name__ == '__main__':

    # standard input
    A, B = map(int, input().split())

    # solve
    solution = Solution()
    print(solution.solve(A, B))
