input_line = input()
Line = input_line.split()
if 500*int(Line[0]) >= int(Line[1]):
  print('Yes')
else:
  print('No')