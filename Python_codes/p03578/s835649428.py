import sys
from collections import Counter
 
N = int(input())
s1 = list(map(int,input().split()))
M = int(input())
s2 = list(map(int,input().split()))
 
c1 = Counter(s1)
c2 = Counter(s2)
 
for k,v in c2.items():
    if k in c1:
        if v > c1[k]:
            print('NO')
            sys.exit()
    else:
        print('NO')
        sys.exit()
print('YES')