s = input()

odd  = [ (c in 'RUD') for i, c in enumerate(s) if i % 2 == 0 ]
even = [ (c in 'LUD') for i, c in enumerate(s) if i % 2 == 1 ]

if all(odd) and all(even):
  print('Yes')
else:
  print('No')
