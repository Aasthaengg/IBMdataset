k = int(input())

if k % 2 == 0:
    num = k ** 2 /4
else:
    base = (k-1) / 2
    num = base * (base + 1)

print(int(num))