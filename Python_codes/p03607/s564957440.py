n = int(input())
a = set()
for i in range(n):
  tmp = int(input())
  if tmp in a: a.discard(tmp)
  else: a.add(tmp)
print(len(a))