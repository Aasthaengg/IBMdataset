# coding: utf-8

# https://atcoder.jp/contests/abc121


def main():
    N, M = map(int, input().split())
    AB = [None] * N
    for i in range(N):
        AB[i] = list(map(int, input().split()))

    AB = sorted(AB, key=lambda x: x[0])

    n_drink = 0
    n_store = 0
    for i in range(N):
        n_drink += AB[i][1]
        n_store = i+1
        if n_drink >= M:
            n_last = M - (n_drink - AB[i][1])
            break

    ans = 0
    for i in range(n_store-1):
        ans += AB[i][0] * AB[i][1]

    ans += AB[n_store-1][0] * n_last

    return ans


print(main())
