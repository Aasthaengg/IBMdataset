p={2,3};n,c,k=5,0,int(input())
while c<k:
  for j in p:
    if n%j==0:n+=1;break
  else:
    p.add(n)
    if n%5==1:print(n,end=" ");c+=1
print()