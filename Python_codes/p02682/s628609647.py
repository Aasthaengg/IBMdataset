A,B,C,K = map(int,input().split())
if K < A + B:
  print(min(K,A))
else:
  print(2*A+B-K)