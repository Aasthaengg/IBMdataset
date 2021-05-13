import sys
from math import gcd

input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    g = A[0]
    for a in A[1:]:
        g = gcd(g, a)

    if max(A) >= K and K % g == 0:
        ans = "POSSIBLE"
    else:
        ans = "IMPOSSIBLE"

    print(ans)


if __name__ == "__main__":
    main()
