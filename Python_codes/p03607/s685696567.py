n = int(input())
a = [int(input()) for _ in range(n)]
aset = set()
for x in a:
  if x not in aset:
    aset.add(x)
  else:
    aset.remove(x)
print(len(aset))