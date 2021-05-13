import sys


def main():
    input = sys.stdin.buffer.readline
    k, x = map(int, input().split())
    ans = [i for i in range(x - k + 1, x + k)]
    print(*ans)


if __name__ == "__main__":
    main()
