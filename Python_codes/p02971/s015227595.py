n=int(input())
a=0
b=0
l=[]
for i in range(n):
  c=int(input())
  l.append(c)
a=max(l)
L=sorted(l)
b=L[-2]
for i in range(n):
  if l[i]==a:
    print(b)
  else:
    print(a)