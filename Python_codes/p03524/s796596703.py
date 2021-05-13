S = input()
from collections import Counter
ctr = Counter(S)

mx = max(ctr.values())
mn = min(ctr.values())
if len(ctr) < 3: mn = 0
if abs(mx-mn) < 2:
    print('YES')
else:
    print('NO')