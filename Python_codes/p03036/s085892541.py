r, D, x_2000 = [int(i) for i in input().strip().split()]

x_prev = x_2000
i = 1
while True:
    x = r * x_prev - D
    print(x)
    x_prev = x
    if i == 10:
        break
    i += 1
