w = list(input())

from collections import Counter

dic = Counter(w)

for i in dic.values():
    if i % 2 == 1:
        print('No')
        break
else:
    print('Yes')