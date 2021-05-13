import math


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N, M = read_ints()
    # M = a*b b >= N
    i = 1
    max_gcd = 1
    while i*i <= M:
        if M%i == 0:
            if M//i >= N:
                max_gcd = max(max_gcd, i)
            if i >= N:
                max_gcd = max(max_gcd, M//i)
        i += 1
    return max_gcd


if __name__ == '__main__':
    print(solve())
