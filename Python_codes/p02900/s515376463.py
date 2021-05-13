from math import gcd
a, b = map(int, input().split())

gcd = gcd(a, b)
ans = 1
n = int(gcd**0.5) + 2
for i in range(2, n):
    if gcd%i == 0:
        ans += 1
        while gcd%i == 0:
            gcd //= i
    if gcd < i:
        break
if gcd >= n:
    ans += 1
if ans == 1 and gcd != 1:
    ans = 2
    
print(ans)