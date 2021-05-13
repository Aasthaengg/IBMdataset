s = input()
g = s[1:]
a = g.replace('9','')
if a == '':
  print(int(s[0])+(len(s)-1)*9)
elif len(s) == 1:
  print(s)
else:
  print(int(s[0])-1+9*(len(s)-1))