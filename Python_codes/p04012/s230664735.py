from collections import Counter
S = list(input())

C = Counter(S)

ok = True
for s,x in C.items():
  if x % 2 != 0:
    ok = False
    break

if ok:
  print("Yes")
else:
  print("No")
