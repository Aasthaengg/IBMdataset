import sys

readline = sys.stdin.buffer.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from collections import deque

    h, w, k = map(int, readline().split())

    if w == 1:
        print(1)
        sys.exit()

    que = deque("0")
    com = {i: {j: 0 for j in (-1, 0, 1)} for i in range(1, w + 1)}

    while que:
        cur = que.popleft()

        if len(cur) == w:
            cur += "0"
            for col in range(1, w + 1):
                if col >= 2 and cur[col - 1] == "1":
                    com[col][-1] += 1
                if col <= w - 1 and cur[col] == "1":
                    com[col][1] += 1
                if cur[col-1] == cur[col] == "0":
                    com[col][0] += 1
        else:
            if cur[-1] == "0":
                que.append(cur + "1")
            que.append(cur + "0")

    dp = [[0] * (w + 1) for _ in range(h + 1)]
    dp[0][1] = 1
    for row in range(h):
        for col in range(1, w + 1):
            if col >= 2:
                dp[row + 1][col - 1] += dp[row][col] * com[col][-1]
                dp[row + 1][col - 1] %= MOD
            if col <= w - 1:
                dp[row + 1][col + 1] += dp[row][col] * com[col][1]
                dp[row + 1][col + 1] %= MOD
            dp[row + 1][col] += dp[row][col] * com[col][0]
            dp[row + 1][col] %= MOD

    print(dp[-1][k] % MOD)


if __name__ == '__main__':
    main()
