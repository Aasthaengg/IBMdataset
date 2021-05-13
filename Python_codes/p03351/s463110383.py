import sys

input = sys.stdin.readline


def main():
    a, b, c, d = map(int, input().split())
    print("Yes" if abs(a - c) <= d or (abs(a - b) <= d and abs(b - c) <= d) else "No")


if __name__ == "__main__":
    main()
