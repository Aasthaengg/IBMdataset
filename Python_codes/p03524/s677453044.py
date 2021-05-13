#CODEFESTIVAL2017-B
from collections import Counter
s = input()
c = Counter(s)
if len(s) == 1:
    print('YES')
else:
    if abs(c['a']-c['b']) <= 1 and abs(c['b']-c['c']) <= 1 and abs(c['c']-c['a']) <= 1:
        print('YES')
    else:
        print('NO')