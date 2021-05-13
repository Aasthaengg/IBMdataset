import sys
sys.setrecursionlimit(10 ** 6)


def input():
    return sys.stdin.readline()[:-1]


def main():
    n = int(input())
    print(n*(n-1)//2)


if __name__ == "__main__":
    main()
