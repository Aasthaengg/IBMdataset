w, h, x, y = [int(i) for i in input().split()]
pat = 0

if x == w / 2 and y == h / 2:
    pat = 1

print((w * h) / 2, pat)
