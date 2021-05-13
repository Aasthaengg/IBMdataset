w, h, x, y = map(int, input().split())

judge = (w == 2 * x and h == 2 * y)
s = w * h / 2
print(s, 1 if judge else 0)
