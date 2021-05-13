from collections import Counter
d = Counter(list(input()))
a = d['a']
b = d['b']
c = d['c']
if max(a, b, c) - min(a, b, c) >= 2:
    print('NO')
else:
    print('YES')