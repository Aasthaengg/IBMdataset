import math as np
k = int(input())
D = {}
for a in range(1, k + 1):
    for b in range(1, k + 1):
        try:
            D[np.gcd(a, b)] += 1
        except:
            D[np.gcd(a, b)] = 1
ans = 0
for c in range(1, k + 1):
    for key, cnt in D.items():
        ans += cnt * np.gcd(c, key)
print(ans)
