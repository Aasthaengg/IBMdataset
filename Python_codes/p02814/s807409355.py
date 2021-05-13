import math

def lcm(a, b):
    return (a * b) // math.gcd(a, b)
def div2(n):
    return bin(n)[::-1].find("1")

n, m = map(int, input().split())
a = list(map(int, input().split()))
ans = a[0]
count = div2(a[0])
for i in range(1, len(a)):
    if count != div2(a[i]):
        print(0)
        exit()
    ans = lcm(ans, a[i])
ans //= 2
print((m // ans + 1) // 2)