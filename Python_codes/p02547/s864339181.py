c=0
for _ in range(int(input())):
  d,_,e=input()
  if d==e: c+=1
  else: c=0
  if c>2: exit(print('Yes'))
print('No')