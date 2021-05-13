import sys
from itertools import islice


def resolve(in_):
    R, C, K = map(int, next(in_).split())
    _rcv = (map(int, line.split()) for line in islice(in_, K))

    R1 = R + 1
    C1 = C + 1
    R2 = R + 2
    C2 = C + 2
    limit_item = 3
    limit_item1 = limit_item + 1
    C2limit_item1 = C2 * limit_item1

    # grid = [[0] * C2 for _ in range(R2)]
    grid = [0] * (R2 * C2)
    for r, c, v in _rcv:
        # grid[r][c] = v
        grid[(r * C2) + c] = v

    
    # dp = [[[0] * limit_item1 for j in range(C2)] for i in range(R2)]
    dp = [0] * (R2 * C2 * limit_item1)
    # dp[1][1][1] = grid[1][1]
    dp[(1 * C2limit_item1) + (1 * limit_item1) + 1] = grid[(1 * C2) + 1]

    for i in range(1, R1):
        for j in range(1, C1):
            for k in range(limit_item1):
                # current = dp[i][j][k]
                current = dp[(i * C2limit_item1) + (j * limit_item1) + k]

                # left = grid[i][j + 1]
                left = grid[(i * C2) + (j + 1)]
                # dp[i][j + 1][k] = max(dp[i][j + 1][k], current)
                dp[(i * C2limit_item1) + ((j + 1) * limit_item1) + k] = max(dp[(i * C2limit_item1) + ((j + 1) * limit_item1) + k], current)
                if k < limit_item:
                    # dp[i][j + 1][k + 1] = max(dp[i][j + 1][k + 1], left + current)
                    dp[(i * C2limit_item1) + ((j + 1) * limit_item1) + (k + 1)] = max(dp[(i * C2limit_item1) + ((j + 1) * limit_item1) + (k + 1)], left + current)

                # top = grid[i + 1][j]
                top = grid[((i + 1) * C2) + j]
                # dp[i + 1][j][0] = max(dp[i + 1][j][0], current)
                dp[(i + 1) * C2limit_item1 + (j * limit_item1) + 0] = max(dp[(i + 1) * C2limit_item1 + (j * limit_item1) + 0], current)
                # dp[i + 1][j][1] = max(dp[i + 1][j][1], top + current)
                dp[(i + 1) * C2limit_item1 + (j * limit_item1) + 1] = max(dp[(i + 1) * C2limit_item1 + (j * limit_item1) + 1], top + current)
    # return max(dp[R][C])
    return max(dp[(R * C2limit_item1) + (C * limit_item1):((R + 1) * C2limit_item1) + ((C + 1) * limit_item1)])


def main():
    answer = resolve(sys.stdin.buffer)
    print(answer)


if __name__ == '__main__':
    main()
