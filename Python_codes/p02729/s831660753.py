N,M=map(int,input().split())
if N<2:
  if M<2:
    print(0)
  else:
    print(int(M*(M-1)//2))
else:
  if M<2:
    print(int(N*(N-1)//2))
  else:
    print(int(N*(N-1)//2)+int(M*(M-1)//2))