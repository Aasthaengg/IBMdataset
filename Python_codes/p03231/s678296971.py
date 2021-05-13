from math import gcd
n, m = map(int, input().split())
s = list(input())
t = list(input())
g = gcd(n, m)
ans = n*m//g
sp_a, sp_b = m//g, n//g
jud = True
for i in range(ans//sp_a):
    if i*sp_a % sp_b == 0:
        if s[i % n] != t[i*sp_a//sp_b]:
            jud = False

if jud:
    print(ans)
else:
    print(-1)