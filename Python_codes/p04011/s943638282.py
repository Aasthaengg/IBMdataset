n, k, x, y = [int(input()) for _ in range(4)]
if n >= k:
    print(x*k + y*(n-k))
else:
    print(x*n)