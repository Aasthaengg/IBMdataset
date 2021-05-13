from fractions import gcd
n, m = map(int, input().split())
s = list(input())
t = list(input())
i = 1
ans = n * m // gcd(n, m)
g = gcd(n, m)
for i in range(g):
    if s[i * n // g] != t[i * m // g]:
        ans = -1
        break
print(ans)
