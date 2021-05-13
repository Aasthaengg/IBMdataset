def abc131c_anti_division():
    import math
    a, b, c, d = map(int, input().split())
    cnt = b // c - ((a - 1) // c)
    cnt += b // d - ((a - 1) // d)
    e = (c * d) // math.gcd(c, d)
    cnt -= (b // e - ((a - 1) // e))
    print(b - a + 1 - cnt)

abc131c_anti_division()