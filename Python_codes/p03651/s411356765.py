from fractions import gcd
n, k = map(int, input().split())
a = list(map(int, input().split()))

a_gcd = a[0]
for i in range(1, n):
    a_gcd = gcd(a_gcd, a[i])
ans = True
if k > max(a):
    ans = False
if k % a_gcd != 0:
    ans = False
if k in a:
    ans = True

print('POSSIBLE' if ans else 'IMPOSSIBLE')