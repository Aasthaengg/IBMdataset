import fractions
n, m = map(int, input().split())
s = input()
t = input()
g = fractions.gcd(n, m)
r = (m*n)//g
n, m = n//g, m//g
for i in range(g):
    if s[i*n] != t[i*m]: r = False
if r: print(r)
else: print(-1)