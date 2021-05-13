S=input()
l=len(S)

for i in range(1<<(l-1)):
  Q=[]
  ans=int(S[0])
  for j in range(l-1):
    if (i>>j)&1:
      Q.append('+')
    else:
      Q.append('-')
  for k in range(l-1):
    if Q[k]=='+':
      ans+=int(S[k+1])
    else:
      ans-=int(S[k+1])
  if ans==7:
    ret=str(S[0])
    for k in range(l-1):
      ret+=Q[k]
      ret+=S[k+1]
    ret+='=7'
    print(ret)
    exit()