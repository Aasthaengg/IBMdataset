def isprime(i):
  j=2
  while(j**2<=i):
    if(i%j==0):
      return False
    j+=1
  return True

n=int(input())
x=[]
for i in range(6,55552,5):
  if(isprime(i)):
    x.append(i)
  if(len(x)==n):
    break
print(*x)