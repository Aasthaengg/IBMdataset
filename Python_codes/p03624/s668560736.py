S = input()
alf = 'abcdefghijklmnopqrstuvwxyz'

s = set()
a = set()

for i in range(len(S)):
  s.add(S[i])
for i in range(len(alf)):
  a.add(alf[i])

str = ''
hoge = a ^ s
for h in hoge:
  str += h
  
str=sorted(str)
if str:
  print(str[0])
else:
  print('None')