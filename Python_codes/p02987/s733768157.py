from collections import Counter

s=input()

c = Counter(list(s))

if list(c.values()) == [2,2]:print('Yes')
else:print('No')