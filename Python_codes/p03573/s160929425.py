x = input().split()
t = ''
if x[0] == x[1]:
  t = x[0]
elif x[1] == x[2]:
  t = x[1]
elif x[0] == x[2]:
  t = x[0]
for i in x:
  if t != i:
    print(i)