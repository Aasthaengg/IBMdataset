A,B = map(int,input().split())
L = B // 2
if A >= 13:
  print(B)
elif A <= 12 and A >= 6:
  print(L)
elif A <= 6:
  print(0)