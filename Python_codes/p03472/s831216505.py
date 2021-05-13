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

    ans = 0
    for b in B:
        H -= b
        ans += 1
        if H <= 0:
            break

    if H > 0:
        ans += (H + Amax - 1) // Amax

    print(ans)
    return


if __name__ == '__main__':
    main()
