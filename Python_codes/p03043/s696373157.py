import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    n, k = input_int_list()
    ans = 0
    for i in range(1, n + 1):
        start = i
        cnt = 0
        while start < k:
            start *= 2
            cnt += 1
        ans += 1 / (n * 2**cnt)
    print(ans)
    return


if __name__ == "__main__":
    main()
