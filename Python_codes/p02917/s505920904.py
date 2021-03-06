import sys


def main():
    input = sys.stdin.buffer.readline
    n = int(input())
    b = list(map(int, input().split()))
    a = [0] * n
    a[0] = b[0]
    for i in range(1, n - 1):
        a[i] = min(b[i - 1], b[i])
    a[n - 1] = b[n - 2]
    print(sum(a))


if __name__ == "__main__":
    main()
