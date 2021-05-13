s = list(input())

import collections
c = collections.Counter(s)
ca = c["a"]
cb = c["b"]
cc = c["c"]
if max(ca,cb,cc) - min(ca,cb,cc) >= 2:
    print("NO")
else:
    print("YES")