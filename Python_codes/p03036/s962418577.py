r, d, x0 = list(map(int, input().split()))
for _ in range(10):
    x = r * x0 - d
    print(x)
    x0 = x
