from fractions import gcd
n = int(input())
lcm_t = int(input())
for i in range(n - 1):
    t = int(input())
    lcm_t = lcm_t * t // gcd(lcm_t, t)
print(lcm_t)