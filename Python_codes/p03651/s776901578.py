import math


def main():
    N, K = list(map(int, input().split(' ')))
    A = list(map(int, input().split(' ')))
    M = max(A)
    g = A[0]
    for a in A[1:]:
        g = math.gcd(g, a)
    if K <= M and K % g == 0:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')


if __name__ == '__main__':
    main()