S=input()
T=input()
for i in range(len(S)-1,len(T)-2,-1):
  a=''
  for j in range(len(T)):
    if S[i+1-len(T)+j]=='?':
      a=a+T[j]
    else:
      a=a+S[i+1-len(T)+j]
  if a==T:
    U=S[:i+1-len(T)]+a+S[i+1-len(T)+len(T):]
    c=''
    for k in range(len(U)):
      if U[k]=='?':
        c=c+'a'
      else:
        c=c+U[k]
    print(c)
    exit()
print('UNRESTORABLE')