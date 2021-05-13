a = input()
n = len(a)
from collections import Counter
c = Counter(a)
ans = (n**2-n)//2
for v in c.values():
    ans -= (v**2-v)//2
print(ans+1)
