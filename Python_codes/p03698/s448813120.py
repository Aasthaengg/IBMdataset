import sys
from collections import Counter
S = list(input())
C = Counter(S)
for k, v in C.items():
    if v != 1:
        print('no')
        sys.exit()
print('yes')
