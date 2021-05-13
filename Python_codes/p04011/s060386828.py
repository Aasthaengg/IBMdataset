n, k, x, y = [int(input()) for i in range(4)]
if n > k:
    syogaku = k * x
    sagaku = (n - k) * y
    print(syogaku + sagaku)
else:
    syogaku = n * x
    print(syogaku)