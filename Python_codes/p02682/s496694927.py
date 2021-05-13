A,B,C,K = map(int,input().split())

if A >= K:
  print(K*1)
else:
  K -= A
  if B >= K:
    print(A*1)
  else:
    K -= B
    print(A*1 + K*(-1))