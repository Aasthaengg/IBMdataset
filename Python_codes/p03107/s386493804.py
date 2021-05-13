S = list(input())
L = len(S)
from collections import Counter
c = Counter(S)
one = c['1']
zero = c['0']

print(L-abs(one-zero))