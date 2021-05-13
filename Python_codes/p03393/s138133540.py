s = input()
l = len(s)
backet = [0] * 26
if l != 26:
  for i in s:
    backet[ord(i) - 97] = 1
  for i in range(26):
    if not backet[i]:
      print(s + chr(i + 97))
      break
else:
  if s == "zyxwvutsrqponmlkjihgfedcba":
    print(-1)
  else:
    d = []
    for i in s[::-1]:
      s = s[:-1]
      d.sort()
      for j in d:
        if j > ord(i)-97:
          print(s + chr(j+97))
          exit()
      d.append(ord(i)-97)
