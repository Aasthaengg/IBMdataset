A,B,C = map(int,input().split())

if A == B == C: 
  print(-1 if A%2==0 else 0)
else:
  c = 0
  while A % 2 == 0 and B % 2 == 0 and C % 2 == 0:
    ba = A
    bb = B
    bc = C
    A = (bb + bc)//2
    B = (ba + bc)//2
    C = (ba + bb)//2
    c+=1
  print(c)
