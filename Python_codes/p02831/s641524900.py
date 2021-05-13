from fractions import gcd

def lcm(a, b):
    res = a*b / gcd(a, b)
    return res

a, b = map(int, input().split())
ans = int(lcm(a, b))
print(ans)