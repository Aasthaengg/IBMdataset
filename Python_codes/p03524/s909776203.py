from collections import Counter

S = input()
C = Counter(S)
C.setdefault('a',0)
C.setdefault('b',0)
C.setdefault('c',0)
C = C.values()
if max(C) - min(C) == 0 or max(C) - min(C) == 1:
    print('YES')
else:
    print('NO')