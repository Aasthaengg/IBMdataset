N, K = map(int, input().split())
list1 = []
if N <= abs(N - K):
  print(N)
  exit()
else:
  N = N % K
  while N > abs(N-K):
    N = abs(N - K)
    list1.append(N)
  
if list1 ==[]:
  print(0)
else:
  print(min(list1))