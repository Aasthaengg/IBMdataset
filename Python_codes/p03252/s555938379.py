# AtCoder
from collections import Counter
S = list(input())
T = list(input())
if sorted(Counter(S).values()) == sorted(Counter(T).values()):
    print('Yes')
else:
    print('No')
