import sys


def main():
    input = sys.stdin.buffer.readline
    n = int(input())
    d = sorted((map(int, input().split())))
    print(d[n // 2] - d[n // 2 - 1])


if __name__ == "__main__":
    main()
