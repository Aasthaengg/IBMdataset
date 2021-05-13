s = input()
if s[0]=='R':
  if s[1]=='R':
    if s[2]=='R':
      print(3)
    else:
      print(2)
  else:
    print(1)
elif s[0]=='S':
  if s[1]=='R':
    if s[2]=='R':
      print(2)
    else:
      print(1)
  else:
    if s[2]=='R':
      print(1)
    else:
      print(0)