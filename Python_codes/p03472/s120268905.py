import sys
from itertools import accumulate
from bisect import bisect_left

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, H, *AB = map(int, read().split())
    A = AB[::2]
    B = AB[1::2]

    Amax = max(A)
    B = [b for b in B if b >= Amax]
    B.sort(reverse=True)
    B = list(accumulate(B))

    i = bisect_left(B, H)
    if i < len(B):
        ans = i + 1
    else:
        ans = len(B) + (H - B[-1] + Amax - 1) // Amax

    print(ans)
    return


if __name__ == '__main__':
    main()
