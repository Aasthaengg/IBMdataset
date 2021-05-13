def intSqrt(n):
    x = 1
    while True:
        x2 = (x + n // x) // 2
        if x2 ** 2 <= n and abs(x - x2) <= 1:
            break
        x = x2
    return x2

n = int(input())
print(intSqrt(n)**2)
