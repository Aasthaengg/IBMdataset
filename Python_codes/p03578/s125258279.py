import sys
from collections import Counter

N = int(input())
d = list(map(int, input().split()))
M = int(input())
t = list(map(int, input().split()))

c = Counter(d)
for i in t:
    if c[i] > 0:
        c[i] -= 1
    else:
        print('NO')
        sys.exit()
print('YES')
    
    
