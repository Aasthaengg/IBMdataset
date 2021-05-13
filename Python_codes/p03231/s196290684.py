def gcd(a, b):
    if a < b:
        a, b = b, a
    while a % b != 0:
        a, b = b, a % b
    return b

def lcm(a, b):
    return a * b // gcd(a, b)

n, m = map(int, input().split())
s = str(input())
t = str(input())
g = gcd(n, m)
l = lcm(n, m)
for i in range(g):
    if s[i*n//g] != t[i*m//g]:
        print(-1)
        break
else:
    print(l)
