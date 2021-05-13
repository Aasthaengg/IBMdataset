N=int(input())
if N%2==0:
  if N-(N/2)==(N/2):
    print(int((N-1)/2))
  else:
    print(int(N/2))
else:
  print(int(((N+1)/2)-1))