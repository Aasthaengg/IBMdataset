# coding: utf-8

# https://atcoder.jp/contests/abc110


def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    x = sorted(x)
    y = sorted(y)

    x_max = max(x)
    y_min = min(y)

    for z in range(X+1, Y+1):
        if x_max < z <= y_min:
            return "No War"
    
    return "War"


print(main())
