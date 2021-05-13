c=0
n=int(input())
for _ in range(n):
 x=int(input())
 if x!=2 and x%2==0:c+=1;continue
 for i in range(3,int(x**.5+1),2):
  if x%i==0:c+=1;break
print(n-c)
