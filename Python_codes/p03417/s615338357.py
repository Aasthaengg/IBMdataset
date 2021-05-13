import sys

input = sys.stdin.readline


def main():
    N, M = [int(x) for x in input().split()]
    if N >= 2 and M >= 2:
        print((N - 2) * (M - 2))
    else:
        if N == 1 == M:
            print(1)
        else:
            print(max(N, M) - 2)


if __name__ == '__main__':
    main()
