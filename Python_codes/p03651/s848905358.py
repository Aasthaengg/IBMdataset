import sys
import fractions

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N, K = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]

    A.sort()

    g = A[0]

    for a in A:
        g = fractions.gcd(g, a)

    for a in A:
        if a >= K:
            if (a - K) % g == 0:
                print("POSSIBLE")
                return
    else:
        print("IMPOSSIBLE")


if __name__ == '__main__':
    main()
