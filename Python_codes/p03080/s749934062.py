from collections import defaultdict
n = int(input())
s = list(input())
c = defaultdict(int)
for ss in s:
    c[ss] += 1
if c['R'] > c['B']:
    print('Yes')
else:
    print('No')