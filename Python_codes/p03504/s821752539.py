class Solution:
    def solve(self, N: int, C: int, stc) -> int:

        p = [[0 for _ in range(2*10**5)] for _ in range(C)]

        for s, t, c in stc:
            for i in range(2*s-1, 2*t):
                p[c-1][i] = 1

        ans = 0
        for i in range(2*10**5):
            q = 0
            for c in range(C):
                q += p[c][i]
            ans = max(ans, q)

        return ans


if __name__ == '__main__':

    # standard input
    N, C = map(int, input().split())
    stc = []
    for _ in range(N):
        stc.append(tuple(map(int, input().split())))

    # solve
    solution = Solution()
    print(solution.solve(N, C, stc))
