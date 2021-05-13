def actual(a, b, c):
    return f'{a[0]}{b[0]}{c[0]}'.upper()

a, b, c = input().split()
print(actual(a, b, c))