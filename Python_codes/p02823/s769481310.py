N, A, B = map(int,input().split())

if (A-B)%2 == 0:
  print(abs(A-B)//2)
else:
  print(min((A+B-1)//2,(2*N-(A+B)+1)//2))