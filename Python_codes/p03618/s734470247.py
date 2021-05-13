from collections import Counter

s = input()
n = len(s)
ans = n * (n - 1) // 2 + 1
c = Counter(s)
for key, value in c.items():
    ans -= value * (value - 1) // 2
print(ans)