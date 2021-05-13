import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    for a in A:
        if a & 1:
            print("first")
            return
    else:
        print("second")


if __name__ == '__main__':
    main()

