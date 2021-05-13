from collections import Counter
a = input()
ct = Counter(a)
_sum = 0
for c in ct.values():
    _sum += c * (c - 1) / 2
print(int(len(a) * (len(a) - 1) / 2 - _sum + 1))