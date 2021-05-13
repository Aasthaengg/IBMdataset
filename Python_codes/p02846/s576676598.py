T1, T2=map(int,input().split())
A1, A2=map(int,input().split())
B1, B2=map(int,input().split())

if A1 - B1 > 0:
  A1, B1 = B1, A1
  A2, B2 = B2, A2
  
d = (A1 - B1) * T1 + (A2 - B2) * T2

if d > 0:
  if ((B1 - A1) * T1) % d == 0:
    print(((B1 - A1) * T1 // d) *  2)
  else:
    print(((B1 - A1) * T1 // d) *  2 + 1)
elif d < 0:
  print(0)
else:
  print("infinity")