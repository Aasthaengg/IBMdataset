# coding: utf-8

# https://atcoder.jp/contests/abc119


def main():
    N = int(input())
    x, u = [None] * N, [None] * N

    for i in range(N):
        line = input().split()
        x[i], u[i] = float(line[0]), line[1]
    
    jpy = 0
    btc = 0.0
    for i in range(N):
        if u[i] == "BTC":
            btc += x[i]
        else:
            jpy += x[i]
    
    return jpy + 380000.0 * btc


print(main())
