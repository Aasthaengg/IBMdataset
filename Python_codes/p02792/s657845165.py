import sys
import numpy as np
input = lambda: sys.stdin.readline().rstrip()


def solve():
    N = int(input())
    d = np.zeros((9, 9), dtype='i8')

    for i in range(1, N + 1):
        s = str(i)
        a = int(s[0])
        b = int(s[-1])
        if a != 0 and b != 0:
            d[a - 1][b - 1] += 1

    ans = 0
    for i in range(9):
        for j in range(9):
            if i == j:
                ans += d[i][j] * (d[i][j] - 1) + d[i][j]
            else:
                ans += d[i][j] * d[j][i]

    # print(d)
    print(ans)


if __name__ == '__main__':
    solve()
