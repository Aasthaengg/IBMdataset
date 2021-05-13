a = int(input())
A = []
n = 1

while True:
  n+=1
  A+=[a]
  
  if a%2==0:
    a//=2
  else:
    a=1+3*a
  
  if a in A:
    print(n)
    break