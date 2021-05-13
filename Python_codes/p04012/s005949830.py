w = input()

from collections import Counter
A = Counter(w)

ans="No"
for k,v in Counter(A).items():
  if v%2==1: break
else:
  ans="Yes"
print(ans)

