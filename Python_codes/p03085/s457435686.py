b = input()
l1 = ['A','T']
l2 = ['C','G']
if b in l1:
  l1.remove(b)
  print(l1[0])
else:
  l2.remove(b)
  print(l2[0])