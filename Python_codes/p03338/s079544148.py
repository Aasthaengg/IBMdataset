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
    ans = 0
    for i in range(1, n):
        x = set(S[:i])
        y = set(S[i:])
        cnt = 0
        for c in x:
            if c in y:
                cnt += 1
        ans = max(cnt, ans)
    print(ans)

    return


if __name__ == "__main__":
    main()
