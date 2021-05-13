import math

k = int(input())

ab = []
ans = 0
for a in range(1,k+1):
    for b in range(1,k+1):
        ab.append(math.gcd(a, b))
for i in ab:
    for c in range(1,k+1):
        ans += math.gcd(i, c)

print(ans)