from math import gcd
#a,bの最大公約数
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

#a,bの最小公倍数
def lcm(a, b):
    return a * b // gcd (a, b)

a, b, c, d = map(int, input().split())
a -= 1
tmp1 = b - (b//c + b//d - b//(lcm(c, d)))
tmp2 = a - (a//c + a//d - a//(lcm(c, d)))

print(tmp1-tmp2)