from collections import Counter
import sys
A = []
for i in range(3):
    a,b = map(int,input().split())
    A.append(a)
    A.append(b)
c = Counter(A)
for i in c.values():
    if i >=3:
        print('NO')
        sys.exit()
print('YES')