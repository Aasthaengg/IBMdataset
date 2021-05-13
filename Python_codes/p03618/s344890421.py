from collections import Counter
s = input()
c = Counter(s)
ans = len(s) * (len(s) - 1) // 2
for v in c.values():
    ans -= v * (v - 1) // 2
print(ans + 1)
