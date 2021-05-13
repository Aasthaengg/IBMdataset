X,A,B = map(int,input().split())

if B-A>=X+1:
  print('dangerous')
elif B-A<=X and A<B:
  print('safe')
elif B<=A:
  print('delicious')
  
  
