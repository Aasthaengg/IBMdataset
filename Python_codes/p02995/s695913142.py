import math
def lcm(x, y): # 最小公倍数
    return (x * y) // math.gcd(x, y)


a, b, c, d = map(int, input().split())

lcm_cd = lcm(c, d)

under_b = b - b//c - b//d + b//lcm_cd
over_a = (a-1) - (a-1)//c - (a-1)//d + (a-1)//lcm_cd

print(under_b - over_a)