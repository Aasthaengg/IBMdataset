#C
n = int(input())
a = list(map(int, input().split()))
#最大公約数
def gcd(a, b):
    while b != 0:
        if a < b:
            b, a = a, b
        a, b = b, a % b
    return a
#最大公倍数
def lcm(a, b):
    return a * b // gcd(a, b)
ans = a[0]
for i in range(1, n):
    ans = gcd(ans, a[i])
print(ans)