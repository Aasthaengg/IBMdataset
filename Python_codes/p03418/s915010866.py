class Solution:

    def solve(self, N: int, K: int) -> int:

        if K == 0:
            return N**2

        answer = 0
        for b in range(K+1, N+1):

            answer += (N//b) * (b-K) + max(N % b-K+1, 0)

        return answer


if __name__ == '__main__':

    # standard input
    N, K = map(int, input().split())
    # solve
    solution = Solution()
    print(solution.solve(N, K))
