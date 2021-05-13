import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    h, n = input_int_list()
    A = input_int_list()
    if sum(A) >= h:
        print("Yes")
    else:
        print("No")
    return


if __name__ == "__main__":
    main()
