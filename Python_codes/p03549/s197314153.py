N, M = [int(x) for x in input().split()]
print((1900 * M + 100 * (N - M)) * 2 ** M)