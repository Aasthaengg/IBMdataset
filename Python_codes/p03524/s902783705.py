from collections import Counter
c = {"a":0,"b":0,"c":0}
for si in input():
    c[si] += 1
if max(c.values()) - min(c.values()) <= 1:
    print("YES")
else:
    print("NO")