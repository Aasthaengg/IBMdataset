import math

a,b=list(map(int,input().split()))
min_num=min(a,b)
gcd=[]

def prime(n):
  if n==1:
    return True
  for i in range(2,int(math.sqrt(n))+1):
    if n%i==0:
      return False
  return True

for i in range(1,int(math.sqrt(min_num)+1)):
  if a%i==0:
    if b%i==0:
      gcd.append(i)
    if b%(a//i)==0:
      gcd.append(a//i)

prime_list=[]
for i in gcd:
  if prime(i):
    prime_list.append(i)
if a==1 or b==1:
  print(len(prime_list)-1)
else:
  print(len(prime_list))


    


      
  
