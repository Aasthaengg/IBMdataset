A,B=map(int, input().split())
if A>=13:
  print(B)
elif A>=6:
  print('{:.0f}'.format(B/2))
else:
  print(0)
