A,B,C,D=map(int,input().split())
turn='t'
while A>0 and C>0:
  if turn=='t':
    C-=B
    turn='a'
  else:
    A-=D
    turn='t'

if A<=0:
  print('No')
else:
  print('Yes')