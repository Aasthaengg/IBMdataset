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

    C = Counter(A)

    total = 0
    for n in C.values():
        total += n * (n - 1) // 2

    ans = [0] * N
    for i, a in enumerate(A):
        ans[i] = total - C[a] + 1

    print('\n'.join(map(str, ans)))
    return


if __name__ == '__main__':
    main()
