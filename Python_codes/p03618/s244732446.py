S = input()
gou = 1
N = len(S)
for i in range(N):
  gou += i
import collections
c = collections.Counter(S)
c = c.items()
for a,b in c:
  gou -= b*(b-1)/2
print(int(gou))
