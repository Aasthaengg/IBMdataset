import sys

input = sys.stdin.readline


def main():
    a, b = map(int, input().split())
    print(a - 1 + int(b >= a))


if __name__ == "__main__":
    main()
