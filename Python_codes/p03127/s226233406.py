# coding: utf-8

# https://atcoder.jp/contests/abc118


def main():
    N = int(input())
    A = list(map(int, input().split()))

    def gcd(n, m):
        """
        2020/05/22
        """
        while True:
            if m == 0:
                return n
            n, m = m, n % m

    for i in range(N-1):
        A[i+1] = gcd(A[i], A[i+1])

    return A[i+1]


print(main())
