c=0
n=int(input())
for _ in range(n):
 x=int(input())
 for i in range(2,int(x**.5+1)):
  if x%i==0:c+=1;break
print(n-c)
