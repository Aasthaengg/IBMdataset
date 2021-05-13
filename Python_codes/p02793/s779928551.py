from functools import reduce

def gcd(x, y):
    if x < y:
        x, y = y, x
    while x % y != 0:
        r = x % y
        x = y
        y = r
    return y

def inv(x):
    return pow(x, MOD-2, MOD)

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_list(l:list):
    return reduce(lcm, l, 1)
  
N = int(input())
a_list = list(map(int, input().split()))
MOD = 10 ** 9 + 7

num = lcm_list(a_list) % MOD
ans = 0
for a in a_list:
    ans += (num * pow(a, MOD-2, MOD)) % MOD

print(ans%MOD)