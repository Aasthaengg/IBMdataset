import sys
from collections import Counter

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, K, *AB = map(int, read().split())
    c = Counter()
    for a, b in zip(*[iter(AB)] * 2):
        c[a] += b

    num = 0
    for k, n in sorted(c.items()):
        num += n
        if num >= K:
            ans = k
            break

    print(ans)
    return


if __name__ == '__main__':
    main()
