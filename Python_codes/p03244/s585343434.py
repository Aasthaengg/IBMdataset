n, *v = map(int, open(0).read().split())
from collections import*
d, e = (Counter(i).most_common()+[(0,0)] for i in (v[0::2], v[1::2]))
print(n-d[0][1]-e[0][1] if d[0] != e[0] else n-max(d[0][1]+e[1][1], d[1][1]+e[0][1]))
