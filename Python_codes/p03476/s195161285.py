def p(x):
  if x<2:
    return 0
  for i in range(2,int(x**0.5)+1):
    if x%i==0:
      return 0
  return 1

C=[0]
for i in range(1,10**5+1):
  C.append(C[-1]+(p(i)&p((i+1)//2)))
l,r=0,0
for i in range(int(input())):
  l,r=map(int,input().split())
  print(C[r]-C[l-1])