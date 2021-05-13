s = input()
r = ""
for i in s:
  if i=='1':
    r += '9'
  elif i=='9':
    r += '1'
print(r)