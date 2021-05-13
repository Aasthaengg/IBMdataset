ret = 0
for x in range(11, int(input()) + 1, 2):
    n = 2
    for y in range(2, x // 2 + 1):
        if x % y == 0:
            n += 1
    if n == 8:
        ret += 1
print(ret)