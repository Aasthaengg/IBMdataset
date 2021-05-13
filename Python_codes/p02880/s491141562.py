import itertools
t = set()
for i, j in itertools.product(range(1, 10), repeat=2):
  t.add(i*j)
n = int(input())
if n in t:
  print("Yes")
else:
  print("No")