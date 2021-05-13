import bisect
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    S = input()
    T = input()
    N = len(S)
    idx = defaultdict(list)
    for i, s in enumerate(S):
        idx[s].append(i)

    # 直前にみたx
    x = -1
    n_loop = 0
    for t in T:
        arr = idx[t]
        if len(arr) == 0:
            print(-1)
            return

        x += 1
        i = bisect.bisect_left(arr, x)
        if i < len(arr):
            x = arr[i]
        else:
            n_loop += 1
            x = arr[0]

    print(n_loop * N + x + 1)


if __name__ == "__main__":
    main()
