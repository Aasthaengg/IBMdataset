import sys
import fractions

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N, K = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]

    A.sort()

    if N == 1:
        if A[0] == K:
            print("POSSIBLE")
        else:
            print("IMPOSSIBLE")
        return

    g = fractions.gcd(A[0], A[1])

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
