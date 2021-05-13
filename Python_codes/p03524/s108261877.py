s=str(input())
s=list(s)
import collections
c=collections.Counter(s)
if max(c["a"],c["b"],c["c"])-min(c["a"],c["b"],c["c"])<=1:
  print("YES")
else:
  print("NO")