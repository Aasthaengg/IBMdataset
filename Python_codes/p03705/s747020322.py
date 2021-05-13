N,A,B=map(int,input().split())
if A>B:
  print(0)
  exit()
if N==1 and A!=B:
  print(0)
  exit()
s=A*(N-1)+B
l=A+B*(N-1)
print(l-s+1)