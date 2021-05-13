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
    A = input_int_list()
    B = input_int_list()
    ans = 0
    for i in range(n):
        ans = max(ans, sum(A[:i + 1]) + sum(B[i:]))
    print(ans)

    return


if __name__ == "__main__":
    main()
