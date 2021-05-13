S=input()
L,R=len(S),-1
for i in range(len(S)):
  if(S[i]=='C'):
    L=i
    break
for i in range(len(S)):
  if(S[len(S)-1-i]=='F'):
    R=len(S)-1-i
    break
if(L<R):
  print("Yes")
else:
  print("No")