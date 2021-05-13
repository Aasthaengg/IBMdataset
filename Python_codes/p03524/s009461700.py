from collections import Counter

S = input()
c = Counter(S)

if abs(c['a'] - c['b']) <= 1 and abs(c['b'] - c['c']) <= 1 and abs(c['c'] - c['a']) <= 1:
    print('YES')
else:
    print('NO')