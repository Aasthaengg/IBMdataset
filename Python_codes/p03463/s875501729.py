N, A, B = list(map(int,input().split()))
empA = (B - A) + 1 
if empA % 2 == 0:
  print('Borys')
else:
  print('Alice')