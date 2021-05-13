N,K = map(int,input().split())

valueA = N % K
valueB = K - valueA

if valueA > valueB:
  print(valueB)
else:
  print(valueA)