import collections

S = [s for s in input()]
k = len(S)
c = collections.Counter(S)
if 15 - k + c["o"] >= 8:
  print("YES")
else:
  print("NO")