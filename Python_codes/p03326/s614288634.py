class Solution:

    def solve(self, N: int, M: int, cakes) -> int:

        sign = []
        for i in [1, -1]:
            for j in [1, -1]:
                for k in [1, -1]:
                    sign.append((i, j, k))

        def sumprod(c, s):
            ret = 0
            for i in range(len(c)):
                ret += c[i] * s[i]
            return ret

        candidates = []
        for s in sign:
            cakes = sorted(cakes, key=lambda c: sumprod(c, s))

            xyz = [0, 0, 0]
            for i in range(M):
                for j in range(3):
                    xyz[j] += cakes[i][j]

            candidates.append(
                sum([abs(xyz_) for xyz_ in xyz])
            )

        return max(candidates)


if __name__ == '__main__':

    # standard input
    N, M = map(int, input().split())
    cakes = []
    for i in range(N):
        cakes.append(tuple(map(int, input().split())))

    # solve
    solution = Solution()
    print(solution.solve(N, M, cakes))
