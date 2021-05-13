x = int(input())
n = (x // 11) * 2
r = x % 11
if 0 < r <= 6:
    n += 1
elif r > 6:
    n += 2
print(n)