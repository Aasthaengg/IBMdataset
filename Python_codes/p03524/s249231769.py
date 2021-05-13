from collections import Counter
s = list(input())

count = Counter(s)
if len(s) <= 3:
  if len(s) == 1: print("YES")
  elif len(count.keys()) == len(s): print("YES")
  else: print("NO")
else:
  if len(count.keys()) <= 2: print("NO")
  elif max(count.values()) - min(count.values()) <= 1: print("YES")
  else: print("NO")
