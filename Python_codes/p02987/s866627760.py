from collections import Counter
s = input()
c = Counter(s)
if len(list(c.items())) == 2 and list(c.items())[0][1] == 2:
    print('Yes')
else:
    print('No')
