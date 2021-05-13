a = input()
from collections import Counter
c = Counter(a)
l = len(a)
ans = l*(l-1)//2+1
for i in c.values():
  ans -= i*(i-1)//2
print(ans)