
import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    n, a, b = input_int_list()
    if b < a or (n == 1 and a != b):
        print(0)
        sys.exit()
    n -= 2
    if n == 0:
        print(1)
    else:
        ans = (b * n) - (a * n) + 1
        print(ans)

    return


if __name__ == "__main__":
    main()
