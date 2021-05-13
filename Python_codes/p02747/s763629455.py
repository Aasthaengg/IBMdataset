S = input()
test = S.split("hi")
rest = ''
for i in test:
  rest += i

if rest == '':
  print('Yes')
else:
  print('No')

