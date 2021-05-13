import math


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N, K = read_ints()
    A = read_ints()
    if K > max(A):
        return 'IMPOSSIBLE'
    gcd = A[0]
    for i in range(1, N):
        gcd = math.gcd(gcd, A[i])
    if K%gcd != 0:
        return 'IMPOSSIBLE'
    return 'POSSIBLE'


if __name__ == '__main__':
    print(solve())
