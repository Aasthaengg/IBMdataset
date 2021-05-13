from collections import Counter
S = input()
d = Counter(S)

na = 0 if "a" not in d.keys() else d["a"]
nb = 0 if "b" not in d.keys() else d["b"]
nc = 0 if "c" not in d.keys() else d["c"]

if abs(na - nb) <= 1 and abs(nc - na) <= 1 and abs(nb - nc) <= 1:
    print("YES")
else:
    print("NO")