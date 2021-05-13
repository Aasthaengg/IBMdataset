from collections import Counter
cnt = Counter()
for i in range(3):
  cnt.update([int(item) for item in input().split()])
a = list(cnt.values())
a.sort()
if a[0] == 1 and a[1] == 1 and a[2] == 2 and a[3] == 2:
  print("YES")
else:
  print("NO")