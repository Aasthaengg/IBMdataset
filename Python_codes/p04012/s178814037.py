import collections
s = input()
c = collections.Counter(s)
c = list(c.values())

for i in range(len(c)):
  if c[i]%2==0:
    c[i]=True
  else:
    c[i]=False

if all(c):
  print('Yes')
else:
  print('No')