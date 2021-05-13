N, M = [int(x) for x in input().split()]


print((M * 1900 + (N - M) * 100) * (2 ** M))
