from collections import Counter
n,m,*ab = map(int,open(0).read().split())
a = Counter(ab)
for i in a.values():
  if i%2 != 0:
    print("NO")
    break
else:
  print("YES")