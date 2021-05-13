S=input()
m=0
b=0
for s in S:
  if s == 'R':
    b+=1
    m=max(m,b)
  else:
    b=0
print(m)