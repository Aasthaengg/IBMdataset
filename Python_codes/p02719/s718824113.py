import sys


def main():
    input = sys.stdin.buffer.readline
    n, k = map(int, input().split())
    n %= k
    while True:
        if abs(n - k) >= n:
            break
        else:
            n = abs(n - k)
    print(n)


if __name__ == '__main__':
    main()
