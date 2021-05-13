s = input()

od = s[0 :: 2]
ev = s[1 :: 2]

if all(x != 'L' for x in od) and all(y != 'R' for y in ev):
  print('Yes')

else:
  print('No')