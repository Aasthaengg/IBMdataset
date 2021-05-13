# coding: utf-8

# https://atcoder.jp/contests/abc112


def yakusu(n):
    ans = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            ans.append(i)
            if n // i != i:
                ans.append(n // i)
    
    return sorted(ans)


def main():
    N, M = map(int, input().split())
    
    xs = yakusu(M)

    for x in reversed(xs):
        if M // x >= N:
            return x


print(main())
