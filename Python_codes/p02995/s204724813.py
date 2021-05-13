a, b, c, d = [int(i) for i in input().split()]

a = a - 1


def gcd(x: int, y: int) -> int:
    if x < y:
        x, y = y, x
    while y > 0:
        r = x % y
        x, y = y, r
    return x


cd = (c * d) // gcd(c, d)

a_c = a // c
b_c = b // c
a_d = a // d
b_d = b // d
a_cd = a // cd
b_cd = b // cd

res = b - (b_c + b_d - b_cd) - (a - (a_c + a_d - a_cd))
print(res)
