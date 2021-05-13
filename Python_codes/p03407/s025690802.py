import sys

input = sys.stdin.readline


def main():
    a, b, c = map(int, input().split())
    print("Yes" if c <= a + b else "No")


if __name__ == "__main__":
    main()
