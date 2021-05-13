a = input()
if len(a) == 2:
  print(a)
else:
  new_str = ''.join(list(reversed(a)))
  print(new_str)