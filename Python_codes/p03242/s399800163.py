s = input()
t = ''
for i in range(3):
  if s[i] == '1':
    t = t + '9'
  elif s[i] == '9':
    t = t + '1'
  else:
    t = t + s[i]
print(t)
