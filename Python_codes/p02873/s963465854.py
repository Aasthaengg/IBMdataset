# https://atcoder.jp/contests/agc040/tasks/agc040_a
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
    ans = 0
    left = 0
    right = 0
    for i in range(len(S) - 1):
        if S[i] + S[i + 1] == "><":
            right += 1
            tmp = max(left, right)
            ans += tmp
            ans += sum([i for i in range(left)])
            ans += sum([i for i in range(right)])
            right = 0
            left = 0
        else:
            if S[i] == ">":
                right += 1
            elif S[i] == "<":
                left += 1
    else:
        if S[-1] == "<":
            left += 1
        else:
            right += 1
        tmp = max(left, right)
        ans += tmp
        ans += sum([i for i in range(left)])
        ans += sum([i for i in range(right)])
    print(ans)
    return


if __name__ == "__main__":
    main()
