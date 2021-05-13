k = int(input())
if k % 2 == 0 or k % 5 == 0:
    x = -1
else:
    x = 1
    y = 7
    z = 7
    while y % k != 0:
        z = (z * 10) % k
        y += z
        x += 1
print(x)