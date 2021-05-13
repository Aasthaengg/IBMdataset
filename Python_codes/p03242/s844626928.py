s = input()
l = []
for i in range(len(s)):
  if s[i] == "1":
    l.append("9")
  elif s[i] == "9":
    l.append("1")
  else:
    l.append(s[i])
for k in l:
  print(k,end="")
