n = int(input())
D = list(map(int, input().split()))
m = int(input())
T = list(map(int, input().split()))

from collections import Counter
cntr = Counter(D)
ans = 'YES'
for t in T:
  if cntr.get(t) == None or cntr.get(t) == 0:
    ans = 'NO'
    break
  else:
    cntr[t] -= 1
print(ans)