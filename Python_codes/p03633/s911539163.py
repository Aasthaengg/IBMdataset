n = int(input())
def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a
# 最小公倍数
def lcm(a,b):
    return a // gcd(a,b) * b

ans = 1
for i in range(n):
    t = int(input())
    ans = lcm(ans,t)
print(ans)
