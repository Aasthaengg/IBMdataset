d, n = [int(x) for x in input().split()]
print(100 ** d * n if n < 100 else 100 ** d * 101)