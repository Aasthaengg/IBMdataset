# https://atcoder.jp/contests/agc022/tasks/agc022_a

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
    if S == "zyxwvutsrqponmlkjihgfedcba":
        print(-1)
        return
    if len(S) < 26:
        for i in range(ord("a"), ord("z") + 1):
            if chr(i) not in S:
                print(S + chr(i))
                return
    elif len(S) == 26:
        for i in range(25)[::-1]:
            c = S[i]
            ss = S[:i]
            for j in range(ord(c) + 1, ord("z") + 1):
                cc = chr(j)
                if cc not in ss:
                    print(ss + cc)
                    return
        print(-1)

    return


if __name__ == "__main__":
    main()
