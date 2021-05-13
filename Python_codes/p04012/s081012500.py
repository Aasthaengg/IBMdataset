import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(rs())
def rs_(): return [_ for _ in rs().split()]
def ri_(): return [int(_) for _ in rs().split()]

from collections import Counter
c = Counter(rs())
ans = 'Yes'
for i in c.values():
    if i % 2 == 1:
        ans = 'No'
print(ans)