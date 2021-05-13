import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    N = input_int()
    ans = ""
    while N:
        r = N % 2
        if r < 0:
            r += 2
        N = (N - r) // (-2)
        ans += str(r)
    ans = ans[::-1]
    if ans:
        print(ans)
    else:
        print(0)
    return


if __name__ == "__main__":
    main()
