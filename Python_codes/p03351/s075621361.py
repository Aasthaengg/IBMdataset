A,B,C,D=map(int,input().split())
if max(A,C) - min(A,C) <= D:
  print('Yes')
elif max(A,B) - min(A,B) <= D and max(C,B) - min(C,B) <= D:
  print('Yes')
else:
  print('No')