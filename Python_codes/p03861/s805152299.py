import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    a, b, x = input_int_list()
    ans = (b // x) - (a // x)
    if a % x == 0:
        ans += 1
    print(ans)
    return


if __name__ == "__main__":
    main()
