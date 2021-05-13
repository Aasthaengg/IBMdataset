r, g, b, n = map(int, input().split())

rm = n // r
gm = n // g
count = 0
for i in range(rm + 1):
    for j in range(gm + 1):
        if ((n - r * i - g * j) % b == 0 and (n - r * i - g * j) // b >= 0):
            count += 1

print(count)
