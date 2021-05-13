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
    A = sorted(input_int_list())
    ans_a = A[-1]
    ans_b = A[0]
    for a in A:
        tmp = a
        if tmp > ans_a - a:
            tmp = ans_a - a
        if tmp > ans_b:
            ans_b = a
    print(ans_a, ans_b)

    return


if __name__ == "__main__":
    main()
