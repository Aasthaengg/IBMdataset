from collections import Counter
s = list(input())
d = Counter(s)
val = [d["a"], d["b"], d["c"]]
val.sort()
if val[2] - val[0] < 2:
    print("YES")
else:
    print("NO")