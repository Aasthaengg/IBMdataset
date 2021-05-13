def gcd(a, b):
    while b != 0:
        # gcd(a, b) == gcd(b, a%b)
        rem = a % b
        a = b
        b = rem
    return a

a, b = map(int, input().split())
print(gcd(a, b))