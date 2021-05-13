import sys

# sys.stdin = open('a1.in')


def read_int_list():
    return list(map(int, input().split()))


def read_str_list():
    return input().split()


def read_int():
    return int(input())


def read_str():
    return input()


def main():
    n, m = read_int_list()
    res = (n - 1) * (m - 1)
    print(res)

main()
