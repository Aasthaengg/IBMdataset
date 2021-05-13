n = int(input())
s = list(map(str, input().split()))
from collections import Counter
d = Counter(s)
if len(d) == 3:
    print('Three')
else:
    print('Four')