N,A,B,C,D=map(int,input().split())
S=input()
for i in range(B-1,D-1):
  if S[i:i+2]=='##':
    print('No')
    exit() 
for i in range(A-1,C-1):
  if S[i:i+2]=='##':
    print('No')
    exit()
if C>D:
  for i in range(B-2,D-1):
    if S[i:i+3]=='...':
      print('Yes')
      exit()
  print('No')
  exit()
print('Yes')