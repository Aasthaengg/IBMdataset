n = int(input())


def calc():
    for y in range(1, 3501):
        for z in range(1, 3501):
            up = n * y * z
            dn = 4 * y * z - n * (y + z)
            if dn <= 0:
                continue
            if up % dn == 0:
                ans = [y, z, up // dn]
                return ans


ans = calc()
print(*ans, sep=" ")
