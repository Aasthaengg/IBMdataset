# coding: utf-8

# https://atcoder.jp/contests/abc083/tasks/arc088_a
# 17:19-


def main():
    X, Y = map(int, input().split())

    ans = 0
    x = X
    while True:
        if x > Y:
            return ans

        ans += 1
        x *= 2


print(main())
