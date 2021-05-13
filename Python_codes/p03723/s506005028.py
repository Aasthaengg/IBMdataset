A,B,C = map(int,input().split())
if A == B and  B == C and C == A:
  print(-1 if A%2==0 else 0 )
else:
  count = 0
  while(A%2==0 and B%2 == 0 and C%2==0):
    A_ = A
    B_ = B
    A = (B+C)/2
    B = (A_+C)/2
    C = (A_+B_)/2
    count+=1
  print(count)
