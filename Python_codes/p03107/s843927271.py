s = input()
r = 0
b = 0

for i in range(len(s)):
  if s[i] == '0':
    r += 1
  else:
    b += 1
if r > b:
  print(b*2)
else:
  print(r*2)