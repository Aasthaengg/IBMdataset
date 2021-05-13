r, D, x_2000 = map(int, input().split())
x = x_2000
for _ in range(10):
    print(r * x - D)
    x = r * x - D
