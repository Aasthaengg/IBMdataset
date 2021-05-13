from collections import Counter
n = int(input())
c = Counter(list(input()))
if c['R'] > c['B']:
    print('Yes')
else:
    print('No')
