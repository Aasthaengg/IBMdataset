import sys
from collections import Counter
 
A = sys.stdin.readline().strip()
la = len(A)
 
ans = la * (la - 1) // 2 + 1
counter = Counter(A)
for key, count in counter.items():
    if count == 1:
        continue
    ans -= count * (count - 1) // 2
 
print(ans)