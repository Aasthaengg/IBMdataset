s=input()
if len(s)!=26:
  for i in range(26):
    if chr(97+i) not in s:
      print(s+chr(97+i))
      break
else:
  for i in range(25)[::-1]:
    checking=s[i]
    for j in range(ord(checking)+1,123):
      if chr(j) not in s[:i]:
        print(s[:i]+chr(j))
        exit()
  print(-1)