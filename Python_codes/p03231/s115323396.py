from fractions import gcd
n, m = map(int, input().split())
s = input()
t = input()
gcm = gcd(n, m)
lcm = n * m // gcm
for i in range(gcm):
    if s[(n // gcm) * i] != t[(m // gcm) * i]:
        print(-1)
        exit()
print(lcm)