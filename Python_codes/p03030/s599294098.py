n=int(input())

l=[]
for i in range(n):
  a,b=map(str, input().split())
  b=100-int(b)
  if b<10:
    b=str('0')+str(b)
  elif b==100:
    b="999"
  else:
    b=str(b)
  a=a+b
  l.append(a)

l2=sorted(l)

for i in range(n):
  print(l.index(l2[i])+1)