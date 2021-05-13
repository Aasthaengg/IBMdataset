d, n = list(map(int, input().split()))
if n != 100:
    print(n * int(100 ** d))
else:
    print(101 * int(100 ** d))
