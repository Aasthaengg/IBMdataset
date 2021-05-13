s = input()
a = 'Yes'
for i in range(len(s)):
  if i%2==0:
    if s[i]!='R' and s[i]!='U' and s[i]!='D':
      a = 'No'
  else:
    if s[i]!='L' and s[i]!='U' and s[i]!='D':
      a = 'No'
print(a)