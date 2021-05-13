s = []


def name(n):
    n -= 1
    s.append(chr(n % 26 + 97))
    if n // 26 != 0:
        name(n // 26)
    return s[::-1]


print(*name(int(input())), sep="")