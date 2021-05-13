def gen_divs(n):
    divs = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divs.append(i)
            if i != n // i:
                divs.append(n // i)
    return divs


def divthensub(v, div):
    while v % div == 0:
        v //= div
    if v % div == 1:
        return True
    else:
        return False


n = int(input())
if n == 2:
    print(1)
else:
    print(len([i for i in gen_divs(n) if divthensub(n, i)]) + len(gen_divs(n - 1)) + 2)
