N, M = map(int,input().split())
if N>1 and M>1:
  print(N*M-(N*2 + (M-2)*2))
elif N==1 and M>1:
  print(N*M-2)
elif M==1 and N>1:
  print(N*M-2)
else:
  print(1)