from collections import Counter

mod = 10 ** 9 + 7
n = int(input())
s = input()
d = Counter(s)
res = 1
for v in d.values():
    res = res * (v + 1) % mod

print(res - 1)
