n=int(input())
l=list(map(int,input().split()))
l.append(999)
a=l[0]
l.remove(a)
c=1
l2=[]
for i in l:
  if a==i:
    c+=1
  else:
    if c!=1:
      l2.append(c)
    c=1
  a=i
c2=0
for i in l2:
  c2+=i//2
print(c2)