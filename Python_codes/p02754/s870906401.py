N,A,B = map(int,input().split())
con = N % (A + B)
if 0 <= con <= A:
  print(A * (N // (A + B)) + con)
else:
  print(A * ((N // (A + B)  + 1)))