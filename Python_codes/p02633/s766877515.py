def gcd(a: int, b: int) -> int:
    return a if b == 0 else gcd(b, a%b)

def lcm(a: int, b: int) -> int:
    return int(a * b / gcd(a, b))

x = int(input())
print(int(lcm(x, 360) / x))