s = input()

lists = [i for i in s]
sets = set(lists)

if len(sets) != 2:
  print('No')
else:
  if lists.count(lists[0]) == 2:
    print('Yes')
  else:
    print('No')
