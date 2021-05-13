A,B,C,K=map(int,input().split())
if A==B==C:
  print('0')
  exit()
  
else:
  if K%2==0:
    key=A-B
    if key>10**18:
      print('Unfair')
    else:
      print(key)
  else:
    key=B-A
    if key>10**18:
      print('Unfair')
    else:
      print(key)
      
