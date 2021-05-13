s = int(input())

if s == 10 ** 18:
    x1, y1 = 10 ** 9, 0
    x2, y2 = 0, 10 ** 9
else:
    x1 = 10 ** 9
    y1 = 1
    div, mod = divmod(s, x1)
    x2 = x1 - mod
    y2 = div + y1

print(*[0, 0, 10**9, 1, x2, y2])
