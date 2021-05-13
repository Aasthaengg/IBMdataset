A,B,C,K = map(int,input().split())

if abs(B-A) > 10**18:
  print('Unfair')
else:
  if K % 2 == 0:
    print(A-B)
  else:
    print(B-A)