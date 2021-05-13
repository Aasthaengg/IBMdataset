import sys
from collections import Counter

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, K, *A = map(int, read().split())

    counter = Counter(A)
    M = len(counter.keys())
    value = sorted(counter.values())

    ans = 0
    for i in range(M - K):
        ans += value[i]

    print(ans)

    return


if __name__ == '__main__':
    main()
