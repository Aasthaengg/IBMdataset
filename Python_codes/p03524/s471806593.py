from collections import Counter
S = input()
counter = Counter(S)
ca, cb, cc = counter['a'], counter['b'], counter['c']
cabc = [ca, cb, cc]
if max(cabc) - min(cabc) <= 1:
    print('YES')
else:
    print('NO')