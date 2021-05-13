s=input()
k=len(s)
import collections
c = collections.Counter(s)
win = c["o"]

if win+15-k>=8:
  print("YES")
else:
  print("NO")