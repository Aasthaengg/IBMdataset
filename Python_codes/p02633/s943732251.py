def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

x = int(input())
ans = lcm(x, 360) // x
print(ans)