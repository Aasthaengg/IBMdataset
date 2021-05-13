s = input()

if len(s) == 2:
  print(0)
else:
  for l in range(1,len(s)):
    s = s[:len(s)-1]
    if s[:len(s)//2] == s[len(s)//2:]:
      print(len(s))
      break
