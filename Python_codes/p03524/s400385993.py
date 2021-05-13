from collections import Counter
import sys
s = input()
n = len(s)
c = Counter(s)
most_times = 0
for value, times in c.items():
    most_times = max(most_times, times)
if most_times == 1:
    print('YES')
    sys.exit()
can = True
if n%3 == 0 and n//3 < most_times:
    can = False
if n%3 != 0 and n//3 + 1 < most_times:
    can = False
if can:
    print('YES')
else:
    print('NO')

