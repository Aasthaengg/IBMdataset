d, n = map(int, input().split())
if n % 100 == 0:
    print(101 * 100 ** d)
else:
    print(n * 100 ** d)
