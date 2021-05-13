from collections import Counter
s = input().rstrip()
L = len(s)
d = Counter(s)
print(L//2-d["p"])