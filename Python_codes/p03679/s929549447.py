import sys


def input():
    return sys.stdin.readline().strip()
# sys.setrecursionlimit(100000)


def main():
    x, a, b = [int(i) for i in input().strip().split()]
    res = a - b
    if res >= 0:
        print("delicious")
    elif abs(res) > x:
        print("dangerous")
    else:
        print("safe")

    return


if __name__ == "__main__":
    main()
