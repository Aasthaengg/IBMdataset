import sys
from math import gcd

input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    G = A[0]
    for a in A:
        G = gcd(G, a)

    if K <= max(A) and K % G == 0:
        ans = "POSSIBLE"
    else:
        ans = "IMPOSSIBLE"

    print(ans)


if __name__ == "__main__":
    main()
