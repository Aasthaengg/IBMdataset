r, d, x = [int(n) for n in input().split()]
for _ in range(10):
    x = r * x - d
    print(x)