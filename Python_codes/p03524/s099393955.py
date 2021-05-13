s = list(map(str,input()))
from collections import Counter
l = Counter(s)
abc = [l["a"],l["b"],l["c"]]
mx = max(abc)
mi = min(abc)
md = sum(abc)-mx-mi
if mx-mi == 1 or mx-mi == 0:
  print("YES")
else:
  print("NO")