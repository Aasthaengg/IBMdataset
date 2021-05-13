s = input ()
x = 'Yes'
for i in range (4):
  if s.count(s[i]) != 2:
    x = 'No'
    break
print (x)