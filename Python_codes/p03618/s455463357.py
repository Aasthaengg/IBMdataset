a=input()
n=len(a)
from collections import Counter
ca=Counter(a)
ans=(n*(n-1))//2+1
for v in ca.values():
  ans-=(v*(v-1))//2
print(ans)