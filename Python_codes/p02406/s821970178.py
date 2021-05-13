n=int(input())
m=[]
for i in range(1,n+1):
 a=i
 if a%3==0:
  m.append(i)
  continue
 while a>0:
  if a%10==3:
   m.append(i)
   break
  a//=10
print(' ',end='')
print(*m)