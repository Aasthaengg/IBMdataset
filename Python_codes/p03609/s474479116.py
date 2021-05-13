import sys

input = sys.stdin.readline


def main():
    x, t = map(int, input().split())
    print(x - t if x >= t else 0)


if __name__ == "__main__":
    main()
