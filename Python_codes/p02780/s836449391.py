# https://atcoder.jp/contests/abc154/tasks/abc154_d
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
    P = [0] + input_int_list()
    expected_sum = [0] * (n + 1)
    # pre-process
    for i in range(1, n + 1):
        exp = (P[i] + 1) / 2
        expected_sum[i] = expected_sum[i - 1] + exp
    ans = 0
    # query from cusum
    for i in range(k, n + 1):
        ans = max(ans, expected_sum[i] - expected_sum[i - k])
    print(ans)
    return


if __name__ == "__main__":
    main()
