n,a,b=map(int, input().split()) #a1 a2 a3

while True:
  if b-a>1:
    a+=1
  else:
    a-=1
  if a==0:
    print('Borys')
    break
  if b-a>1:
    b-=1
  else:
    b+=1
  if b==n+1:
    print('Alice')
    break