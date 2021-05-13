import math
k = int(input())
dec = {}

for a in range(1, k+1):
    for b in range(1, k+1):
        if math.gcd(a, b) not in dec:
            dec[math.gcd(a,b)] = 1
        else:
            dec[math.gcd(a,b)] += 1
ans = 0
for c in range(1, k+1):
    for d in dec.keys():
        ans += math.gcd(d, c) * dec[d]
print(ans)