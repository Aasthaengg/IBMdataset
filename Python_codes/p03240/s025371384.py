# coding: utf-8

# https://atcoder.jp/contests/abc112


def main():
    N = int(input())

    x, y, h = [None] * N, [None] * N, [None] * N

    for i in range(N):
        x[i], y[i], h[i] = map(int, input().split())

    for cx in range(0, 101):
        for cy in range(0, 101):
            first = True
            notans = False
            for i in range(N):
                # print(cx, cy, i)
                if h[i] > 0:
                    H = h[i] + abs(x[i]-cx) + abs(y[i]-cy)
                    if first:
                        first = False
                        pre_H = H
                    else:
                        if H != pre_H:
                            break
            if H == pre_H:
                for i in range(N):
                    if h[i] == 0:
                        if H - abs(x[i]-cx) - abs(y[i]-cy) > 0:
                            notans = True
                            break

                if notans:
                    continue

                print(cx, cy, H)
                return None


main()
# print(main())
