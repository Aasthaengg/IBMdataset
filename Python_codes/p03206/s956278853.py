import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    n = input_int()
    if n == 25:
        print("Christmas")
    elif n == 24:
        print("Christmas Eve")
    elif n == 23:
        print("Christmas Eve Eve")
    elif n == 22:
        print("Christmas Eve Eve Eve")
    return


if __name__ == "__main__":
    main()
