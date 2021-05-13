s = str(input())
t = str(input())

from collections import Counter
cs = Counter(s)
ct = Counter(t)

cs = list(cs.values())
ct = list(ct.values())

cs.sort()
ct.sort()

if cs == ct:
    print('Yes')
else:
    print('No')
