import sys
from fractions import gcd

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N, M = map(int, input().split())
    S = input()
    T = input()
    L = M // gcd(M, N) * N
    G = gcd(M, N)
    n = N // G
    m = M // G

    for i in range(G):
        if S[n * i] == T[m * i]:
            continue
        else:
            print(-1)
            return

    print(L)


if __name__ == "__main__":
    main()
