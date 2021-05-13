from collections import Counter
S = input()
C = Counter(S)
print(min(C['0'], C['1'])*2)
