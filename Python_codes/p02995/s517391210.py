import math

a, b, c, d = map(int, input().split())

def f(n, c, d):
    sum = n
    sum -= n // c
    sum -= n // d
    lcm = c * d // math.gcd(c, d)
    sum += n // lcm
    return sum

ans = f(b, c, d) - f(a-1, c, d)
print(ans)
