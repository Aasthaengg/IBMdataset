n, m = map(int, input().split())
s = input()
t = input()
def gcd(a, b):
    if b == 0: return a
    if a < b: a, b = b, a
    return gcd(b, a%b)
def lcm(a, b):
    return a*b//gcd(a, b)
x = ""
nm = lcm(n, m)
N = {}
M = {}
for i in range(n):
    N[(nm//n)*i] = s[i]
for i in range(m):
    M[(nm//m)*i] = t[i]
if n > m:
    n, m = m, n
    N, M = M, N
f = True
g = lcm(nm//n, nm//m)
for i in N.keys():
    if i % g == 0:
        if N[i] != M[i]:
            f = False
if f: print(nm)
else: print(-1)
