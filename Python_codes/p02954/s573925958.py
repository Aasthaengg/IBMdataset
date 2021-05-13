import sys
from itertools import groupby

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    S = readline().strip()
    N = len(S)

    s = 0
    ans = [0] * N
    for k, g in groupby(S):
        n = len(list(g))
        if k == 'R':
            ans[s + n - 1] += n - n // 2
            ans[s + n] += n // 2
        else:
            ans[s] += n - n // 2
            ans[s - 1] += n // 2
        s += n

    print(*ans)
    return


if __name__ == '__main__':
    main()
