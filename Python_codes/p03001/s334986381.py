w, h, x, y = list(map(int, input().split()))
res = 0
s = w * h / 2
if x == w / 2 and y == h / 2:
    res = 1
print("%s %s" % (s, res))
