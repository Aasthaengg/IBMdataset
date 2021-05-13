r, d, x = list(map(int, input().split()))

for i in range(1, 11):
    y = r * x - d
    print(y)
    x = y