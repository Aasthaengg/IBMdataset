x = int(input())

# 6 -> 5- > 6 -> ....が最適？
p, q = divmod(x, 11)
p *= 2
if q != 0:
    if q <= 6:
        p += 1
    else:
        p += 2

print(p)
