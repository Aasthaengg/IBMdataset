a=list(input())
c=[]
for i in a:
  if i=='+':
    i=1
    c.append(i)
  else:
    i=-1
    c.append(i)
print(sum(c))
