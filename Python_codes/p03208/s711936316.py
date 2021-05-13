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
    H = []
    for _ in range(n):
        H.append(input_int())
    H = sorted(H)
    ans = float("inf")
    for i in range(n - k + 1):
        ans = min(ans, H[i + k - 1] - H[i])
    print(ans)

    return


if __name__ == "__main__":
    main()
