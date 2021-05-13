n=int(input())

a=0
b=0
c=0

for i in range(1,n//3+1):
  a+=3*i

for i in range(1,n//5+1):
  b+=5*i
 
for i in range(1,n//15+1):
  c+=15*i
  
print(int(1/2*n*(n+1)-(a+b-c)))
