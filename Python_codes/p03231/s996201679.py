import math

n, m = map(int, input().split())
s = input()
t = input()

gcd = math.gcd(n, m)
N = n // gcd
M = m // gcd
ans = n * m // gcd
for i in range(gcd):
    if s[i*N] != t[i*M] :
        ans = -1
        break
print(ans)