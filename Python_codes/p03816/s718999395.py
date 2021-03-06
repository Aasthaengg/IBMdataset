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

    odd = even = 0
    for v in counter.values():
        if v % 2 == 0:
            even += 1
        else:
            odd += 1

    if even % 2 == 0:
        ans = odd + even
    else:
        ans = odd + even - 1

    print(ans)
    return


if __name__ == '__main__':
    main()
