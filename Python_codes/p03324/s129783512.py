d, n = map(int, input().split())
if n == 100:
    print(max(100 ** d, 1) * n + 100**d)
else:
    print(max(100 ** d, 1) * n)