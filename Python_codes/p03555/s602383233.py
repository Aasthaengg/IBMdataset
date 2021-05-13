s=input()
t=input()
b = True
for i in range(3):
  if s[i]!=t[2-i]:
    b=False
if not b:
  print('NO')
else:
  print('YES')