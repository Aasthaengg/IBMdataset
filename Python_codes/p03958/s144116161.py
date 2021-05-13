import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    k, t = input_int_list()
    A = input_int_list()
    _max = max(A)
    ans = (_max - (k - _max)) - 1
    if ans < 0:
        ans = 0
    print(ans)
    return


if __name__ == "__main__":
    main()
