a, b, x = map(int, input().split())
x_min = (a - 1) // x
x_max = b // x
if x_max >= x_min:
    print(x_max - x_min)