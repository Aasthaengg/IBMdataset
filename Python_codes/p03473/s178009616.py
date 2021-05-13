import sys
input = sys.stdin.readline
# sys.setrecursionlimit(100000)


def main():
    M = int(input().strip())
    return (24 - M) + 24


if __name__ == "__main__":
    print(main())
