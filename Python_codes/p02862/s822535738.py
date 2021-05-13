p = 10 ** 9 + 7
x, y = map(int, input().split())

diff = abs(x - y)
large = max(x, y)
small = min(x, y)

if (small * 2 < large):
    print(0)
    exit()


# ans = diff
large -= diff * 2
small -= diff

if (small % 3 != 0):
    print(0)
    exit()


num = int(small / 3)
nn = int(num * 2 + diff)
# rr = num

factorial = [0] * (nn + 1)
factorial[0] = 1
for i in range(nn):
    factorial[i + 1] = factorial[i] * (i + 1) % p


def cmb(n, k):
    # if (n == 1 or k == 1):
    if (n == 0 or k == 0):
        return 1
    if (n < 0 or k < 0):
        return 0

    return factorial[n] * pow(factorial[n - k], p - 2, p) * pow(factorial[k], p - 2, p) % p


ans = cmb(int(nn), int(num))
print(int(ans))
