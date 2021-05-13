s = input()
res = ''
for i in s:
  if i == '1':
    res += '9'
  else:
    res += '1'
print(res)