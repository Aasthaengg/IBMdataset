n = int(input())

otosidama = 0.0
bit = 380000
for i in range(n):
    x, v = input().split()

    if v == 'JPY':
        otosidama += float(x)
    else:
        otosidama += float(x) * bit
print(otosidama)
