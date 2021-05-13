s = input()

alphabets = 'abcdefghijklmnopqrstuvwxyz'
for i in s:
  alphabets = alphabets.replace(i, '')
  s = s.replace(i, '')

alphabets = [i for i in alphabets]
alphabets.sort()
if len(alphabets) > 0:
  print(alphabets[0])
else:
  print('None')