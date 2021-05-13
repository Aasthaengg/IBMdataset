import sys

input = sys.stdin.readline


def main():
    N, A, B = map(int, input().split())
    max_XY = min(A, B)
    min_XY = max(A + B - N, 0)
    print("{} {}".format(max_XY, min_XY))


if __name__ == "__main__":
    main()
