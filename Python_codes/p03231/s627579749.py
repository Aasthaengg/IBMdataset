from math import gcd
n, m = map(int, input().split()); s = input(); t = input()
g = gcd(n, m); a = 0
for i in range(g):
    if s[len(s)//g*i] != t[len(t)//g*i]: a = 1; break
print(n*m//g) if a == 0 else print(-1)