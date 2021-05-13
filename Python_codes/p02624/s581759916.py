from collections import Counter
import sys

sys.setrecursionlimit(10 ** 6)

mod = 1000000007
inf = int(1e18)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def inverse(a):
    return pow(a, mod - 2, mod)


def main():
    k = int(input())
    ans = 0
    for i in range(1, k+1):
        ans += k//i * (2 * i + (k//i - 1) * i) // 2
    print(ans)
main()
