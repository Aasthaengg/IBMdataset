Sp=list(input())
Tp=list(input())
L=len(Sp)
K=len(Tp)
for i in reversed(range(L-K+1)):
  for j in range(K):
    a=Sp[i+j]
    b=Tp[j]
    if a!='?' and a!=b:
      break
  else:
    for j in range(K):
      Sp[i+j]=Tp[j]
    break
else:
  print('UNRESTORABLE')
  exit()
for i in range(L):
  if Sp[i]=='?':
    Sp[i]='a'
print(''.join(Sp))