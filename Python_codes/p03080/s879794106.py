from collections import Counter
input()
s = list(input())
cs = Counter(s)

if cs["R"] > cs["B"]:
  print("Yes")
else:
  print("No")