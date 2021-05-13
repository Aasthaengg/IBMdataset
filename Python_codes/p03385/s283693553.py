s = input()
t = set(['a', 'b', 'c'])
u = set()
for i in s:
  u.add(i)
print('Yes' if t == u else 'No')