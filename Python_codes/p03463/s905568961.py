N,A,B=map(int, input().split())
turn=0
while A!=1 and B!=N or turn==0:
  if A!=B-1:
    A+=1
  else:
      A=A-1
  if A<1:
      A=1
  if B!=A+1:
    B=B-1
  else:
    B=B+1
  if B>N:
      B=N
  turn+=1
if A==1:
  print('Borys')
else:
  print('Alice')