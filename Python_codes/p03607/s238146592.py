import sys
from collections import defaultdict

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *A = map(int, read().split())

    d = defaultdict(bool)
    for a in A:
        if d[a]:
            d[a] = False
        else:
            d[a] = True

    ans = sum(1 for f in d.values() if f)
    
    print(ans)
    return


if __name__ == '__main__':
    main()
