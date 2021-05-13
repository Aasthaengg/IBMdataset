import sys
import itertools


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    h, w, K = list(map(int, readline().split()))
    if w == 1:
        print(1)
    else:
        pt = [[0] * w for _ in range(w)]
        pf = [0] * w
        for it in itertools.product([True, False], repeat=w-1):
            b = True
            for i in range(1, len(it)):
                if it[i] and it[i-1]:
                    b = False
                    break
            if b:
                for i in range(len(it)):
                    if it[i]:
                        pt[i][i+1] += 1
                        pt[i+1][i] += 1
                    else:
                        if i == 0:
                            pf[i] += 1
                        elif i == w - 2:
                            pf[i+1] += 1
                for i in range(1, w - 1):
                    if not it[i-1] and not it[i]:
                        pf[i] += 1
        dp = [[0] * w for _ in range(h + 1)]
        dp[0][0] = 1
        for i in range(1, h + 1):
            for j in range(w):
                for k in range(w):
                    if j != k:
                        dp[i][j] += dp[i-1][k] * pt[j][k]
                    else:
                        dp[i][j] += dp[i-1][k] * pf[j]
                    dp[i][j] %= mod
        print(dp[-1][K-1])


if __name__ == '__main__':
    solve()
