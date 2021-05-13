X=int(input())
a=0
b=0
for i in range(1,10**6):
  b+=i
  a+=1
  if X<=b:
    print(a)
    exit()