n,l=[int(x) for x in input().split()]
a=l
pie=0
app=[]
for i in range(n):
  apple=l+i
  pie+=apple
  app.append(apple)
b=[]
for i in app:
  j=abs(i)
  b.append(j)
c=min(b)
d=b.index(c)
pie-=app[d]
print(pie)