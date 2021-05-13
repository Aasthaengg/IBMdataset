import sys


def input():
    return sys.stdin.readline().strip()
# sys.setrecursionlimit(100000)


def main():
    n = int(input().strip())
    A = [int(i) for i in input().split()]
    print(sum(A) - n)

    return


if __name__ == "__main__":
    main()
