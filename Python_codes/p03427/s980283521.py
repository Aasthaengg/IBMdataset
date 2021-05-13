s=input()
if len(s) == 1:
  print(s)
else:
  print(max((len(s)-1)*9+int(s[0])-1,sum([int(s[i]) for i in range(len(s))])))