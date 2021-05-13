from fractions import gcd
#from math import gcd

def lcm(x, y):
    return (x * y) // gcd(x, y)

n, m = map(int, input().split())
s = input()
t = input()
L = gcd(n,m)
ans = lcm(n,m)
for i in range(L):
    if not s[n//L*i] == t[m//L*i]:
        ans = -1
        break
print(ans)