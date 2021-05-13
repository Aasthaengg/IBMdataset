# coding: utf-8

# https://atcoder.jp/contests/abc112


def main():
    N, T = map(int, input().split())
    c = [None] * N
    t = [None] * N
    for i in range(N):
        c[i], t[i] = map(int, input().split())

    costs = []
    for i in range(N):
        if t[i] <= T:
            costs.append(c[i])

    if len(costs) == 0:
        return "TLE"
    
    return min(costs)


print(main())
