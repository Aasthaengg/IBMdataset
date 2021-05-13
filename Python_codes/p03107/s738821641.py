s=list(input())
from collections import Counter
d=Counter(s)
print(min(d["0"], d["1"])*2)