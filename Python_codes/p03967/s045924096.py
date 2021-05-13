from collections import Counter

s = input()
n = len(s)
c = Counter(s)
can_p = n // 2
print(can_p-c['p'])
