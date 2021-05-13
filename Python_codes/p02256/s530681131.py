def gcd(a, b):
    return gcd(b, a % b) if a % b else b

print(gcd(*map(int, input().split())))