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
    S = input()
    x = 0
    ans = 0
    for s in S:
        if s == "I":
            x += 1
        else:
            x -= 1
        ans = max(x, ans)
    print(ans)
    return


if __name__ == "__main__":
    main()
