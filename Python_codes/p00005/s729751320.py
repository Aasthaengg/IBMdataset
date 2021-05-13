def gcd(n, m):
    while n:
        n, m = m % n, n
    return m

while 1:
    try:
        n, m = map(int, input().split())
        g = gcd(n, m)
        print(g, int(n*m/g))
    except EOFError:
        break