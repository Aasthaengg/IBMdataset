import sys
from itertools import accumulate

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *A = map(int, read().split())

    csum = [0]
    csum.extend(accumulate(A))

    ans = INF
    for i in range(1, N):
        tmp = abs(csum[i] - (csum[N] - csum[i]))
        if ans > tmp:
            ans = tmp

    print(ans)
    return


if __name__ == '__main__':
    main()
