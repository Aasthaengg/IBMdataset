input()
S = input()
x = 0
m = 0
for i in S:
  if i == 'I':
    x += 1
  else:
    x -= 1
  m = max(m,x)
print(m)