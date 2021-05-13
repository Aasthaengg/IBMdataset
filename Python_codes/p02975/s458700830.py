n = int(input())
A = list(map(int, input().split()))
from collections import Counter
cntr = Counter(A)
ans = 'No'
if len(set(A)) == 1 and A[0] == 0:
  ans = 'Yes'
elif n % 3 == 0:
  if len(cntr) == 3:
    k = list(cntr.keys())
    v = list(cntr.values())
    if k[0]^k[1]^k[2] == 0 and v[0] == v[1] and v[1] == v[2]:
      ans = 'Yes'
  elif len(cntr) == 2:
    if sorted(cntr.keys())[0] == 0 and cntr.get(0) == n//3:
      ans = 'Yes'
print(ans)