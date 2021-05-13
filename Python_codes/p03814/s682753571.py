s = list(str(input()))

f = ''
for i in s:
  if f == '':  
    if i == 'A':
      f = s.index(i)
  else:
    break  

for i in range(len(s)):
  if s[i] == 'Z':
    e = i

print(e - int(f) + 1)