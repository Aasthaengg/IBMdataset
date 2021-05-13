A, B = map(int, input().split())

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
def lcm(a, b):
    return a // gcd(a, b) * b

ans = lcm(A, B)
print(ans)
