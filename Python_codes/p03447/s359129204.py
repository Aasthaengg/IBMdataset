s = [int(input()) for _ in range(3)]
x, a, b = s[0], s[1], s[2]
if 1 <= a <= 1000 and 1 <= b <= 1000 and a + b <= x <= 10000:
    y = x - a
    z = y % b
    print(z)
