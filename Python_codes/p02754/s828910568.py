N, A, B = map(int, input().split())

if A==B==0:
  print(0)
else:
  r = N%(A+B)
  q = N//(A+B)
  if r<=A:
    print(q*A + r)
  else:
    print((q+1)*A)
