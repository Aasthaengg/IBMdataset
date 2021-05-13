S = input()
from collections import Counter
C = Counter(S)
A = [C['a'], C['b'], C['c']]
print("YES" if max(A) - min(A) < 2 else "NO")