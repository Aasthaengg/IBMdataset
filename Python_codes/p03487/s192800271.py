import sys
from collections import Counter

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *A = map(int, read().split())

    counter = Counter(A)

    ans = 0
    for k, v in counter.items():
        if k > v:
            ans += v
        elif k < v:
            ans += v - k

    print(ans)
    return


if __name__ == '__main__':
    main()
