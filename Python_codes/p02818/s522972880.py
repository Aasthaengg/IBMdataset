A,B,N = map(int,input().split())
if A>=0:
  if N<=A:
    print(A-N,B)
  else:
    N = N-A
    if N<=B:
      print(0,B-N)
    else:
      print(0,0)