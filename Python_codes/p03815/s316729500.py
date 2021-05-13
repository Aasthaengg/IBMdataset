x = int(input())
a = x // 11 * 2
b = x % 11

if 0 < b <= 6:
    a += 1
elif b > 6:
    a += 2

print(a)