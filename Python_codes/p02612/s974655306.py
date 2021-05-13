n = int(input())
if n % 1000 == 0:
    x = n // 1000
else:
    x = (n // 1000) + 1

print((1000 * x) - n)