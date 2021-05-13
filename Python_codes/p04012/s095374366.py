import sys
from collections import Counter
c = Counter(input())
for i in c.most_common():
    if i[1]%2 == 1:
        print('No')
        sys.exit()
print('Yes')

