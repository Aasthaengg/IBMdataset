x=input()
n=len(x)
s=0
for i in x:
  if s and i=='T':s-=1
  if i=='S':s+=1
print(2*s)