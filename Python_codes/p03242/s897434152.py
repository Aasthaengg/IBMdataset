s = input()
l = []
for i in range(3):
  l += s[i]
for i in range(3):
  if l[i] == '1':
    l[i] = '9'
  elif l[i] == '9':
    l[i] = '1'
print(l[0] + l[1] + l[2])