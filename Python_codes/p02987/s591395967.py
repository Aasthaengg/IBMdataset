s = input()
if s[0] == s[1] == s[2] == s[3]:
  print('No')
else:
  if s[0] == s[1]:
      if s[2] == s[3]:
        print('Yes')
      else:
        print('No')
  elif s[0] == s[2]:
      if s[1] == s[3]:
        print('Yes')
      else:
        print('No')
  elif s[0] == s[3]:
      if s[1] == s[2]:
        print('Yes')
      else:
        print('No')
  else:
    print('No')