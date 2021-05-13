def GCD(m, n):
    while n:
        m, n = n, m % n
    return m

while True:
    try:
        a, b = map(int, input().split())
    except:
        break
    if a < b:
        a, b = b, a
    gcd = GCD(a, b)
    lcm = (a * b) // gcd
    print(gcd, lcm)