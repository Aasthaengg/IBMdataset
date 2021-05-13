import sys
from itertools import product

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N, A, B, C = map(int, input().split())
    L = [int(input()) for _ in range(N)]
    P = product(range(4), repeat=N)

    # 0 -> not used
    # 1 -> A
    # 2 -> B
    # 3 -> C
    ans = INF
    for pattern in P:
        mp = 0
        a = 0
        b = 0
        c = 0
        for i, p in enumerate(pattern):
            if p == 0:
                continue
            elif p == 1:
                if a != 0:
                    mp += 10
                a += L[i]
            elif p == 2:
                if b != 0:
                    mp += 10
                b += L[i]
            else:
                if c != 0:
                    mp += 10
                c += L[i]

        if a == 0 or b == 0 or c == 0:
            continue

        mp += abs(A - a)
        mp += abs(B - b)
        mp += abs(C - c)

        if mp < ans:
            ans = mp

    print(ans)


if __name__ == "__main__":
    main()
