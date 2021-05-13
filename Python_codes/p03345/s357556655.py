A,B,C,K = map(int,input().split())
if A - B > 10**18 or B - A > 10**18:
  print('Unfair')
elif K % 2 == 0:
  print(A - B)
elif K % 2 == 1:
  print(B - A)
  
