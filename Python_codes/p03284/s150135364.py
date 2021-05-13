N,K = map(int,input().split(" "))

if N%K == 0:
  print(0)
if N%K != 0:
  print(1)