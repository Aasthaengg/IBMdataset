d, n = [int(x) for x in input().split()]
print(100 ** d * (n + [0, 1][n == 100]))