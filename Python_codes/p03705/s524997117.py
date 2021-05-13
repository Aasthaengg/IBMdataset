import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N, A, B = [int(x) for x in input().split()]

    if A > B:
        print(0)
        return
    if N == 1 and A != B:
        print(0)
        return

    mi = A + B + (N - 2) * A
    ma = A + B + (N - 2) * B
    print(ma - mi + 1)

    

if __name__ == '__main__':
    main()

