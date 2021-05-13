n = int(input())
nums = [int(i) for i in input().split()]
mod = 10 ** 9 + 7

def gcd(x, y): #GCD
    # greatest_common_divisor
    if x < y:
        x, y = y, x
    if y == 0:
        return 0
    if x % y == 0:
        return y
    return gcd(y, x % y)

def lcm(x, y): #LCM
    # lowest_common_multiple
    return x * y // gcd(x, y)

LCM = 1
for num in nums:
    LCM = lcm(num, LCM)
LCM %= mod
# ans = 0
# for num in nums:
#     ans += (LCM // num) % mod
# print(ans % mod)
ans = 0
for num in nums:
    ans += LCM * pow(num, mod - 2, mod)
    ans %= mod

print(ans % mod)