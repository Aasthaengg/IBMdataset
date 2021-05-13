def gcd(n, m):
    while n!=0:
        tmp = n
        n = m % n
        m = tmp
    return m

while 1:
    try:
        n, m = map(int, input().split())
        x = gcd(n, m)
        print(x, int(n*m/x))
    except EOFError:
        break