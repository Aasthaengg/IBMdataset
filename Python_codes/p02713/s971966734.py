import sys
from math import gcd

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    K = int(readline())

    ans = 0
    for a in range(1, K + 1):
        for b in range(1, K + 1):
            g = gcd(a, b)
            for c in range(1, K + 1):
                ans += gcd(g, c)

    print(ans)
    return


if __name__ == '__main__':
    main()
