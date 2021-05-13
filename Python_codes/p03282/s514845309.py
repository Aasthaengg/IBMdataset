import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    S = input()
    k = input_int()
    one = 0
    for s in S:
        if s == "1":
            one += 1
        else:
            tmp = s
            break
    if k <= one:
        print(1)
    else:
        print(tmp)

    return


if __name__ == "__main__":
    main()
