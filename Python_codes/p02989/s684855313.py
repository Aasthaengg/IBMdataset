import sys


def main():
    n = int(sys.stdin.readline())
    d = list(map(int, sys.stdin.readline().split()))
    d.sort()
    h = n // 2
    print(d[h] - d[h - 1])


if __name__ == "__main__":
    main()