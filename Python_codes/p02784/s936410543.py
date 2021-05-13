import sys


def main():
    input = sys.stdin.buffer.readline
    h, _ = map(int, input().split())
    a = list(map(int, input().split()))
    print("Yes" if sum(a) >= h else "No")


if __name__ == "__main__":
    main()
