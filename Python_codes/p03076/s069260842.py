l=[]
m=[]
for i in range(5):
  i = int(input())
  k = 10 - (i%10)
  l.append(i)
  if k != 10:
    m.append(k)
m.sort()
if len(m)==0:
  print(sum(l))
else:
  s = sum(m)-m[-1]
  print(sum(l)+s)