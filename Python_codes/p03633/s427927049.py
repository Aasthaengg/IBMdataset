import math

def lcm(x,y):
    return (x * y) // math.gcd(x,y)

n = int(input())
t = []

for i in range(n):
    t.append(int(input()))

ans = t[0]

for i in t:
    ans = lcm(ans, i)

print(ans)