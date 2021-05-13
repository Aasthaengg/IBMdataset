import collections

s = input()

count = collections.Counter(s)

_max = 0
for i in count.values():
  if _max < i:
    _max = i
if _max >= 2:
  print("no")
else:
  print("yes")