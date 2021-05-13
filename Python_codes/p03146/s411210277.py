S = int(input())

a =S
A =[]
i = 1

while True:
  i +=1
  A += [a]
  a = int(a/2 if a%2==0 else 3*a+1)
  if a in A:
    break

print(i)