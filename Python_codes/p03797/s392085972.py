S,M=map(int,input().split())
if S<(M//2):
  if (M-2*S)<4:
    print(S)
  else:
    print(S+((M-2*S)//4))
else:
  print(M//2)