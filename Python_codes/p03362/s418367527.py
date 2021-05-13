n = int(input())
l = []

def prime(n):
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      return False
  else:
    return True
    

for i in range(2,55556):
  if prime(i) and i%5==1:
    l.append(i)
for i in range(n):
  print(l[i],end=" ")