S=input()
T=input()
s=len(S)
t=len(T)
cand=[[] for _ in range(s-t+1)]
#Tの入る場所によって場合分け
for i in range(s-t+1):
  S_can=[S[k] for k in range(s)]
  for j in range(t):
    if S[i+j]!=T[j] and S[i+j]!='?':
      break
  else:
    for k in range(t):
      S_can[i+k]=T[k]
    for k in range(s):
      if S_can[k]=='?':
        S_can[k]='a'
    cand[i]=S_can
ans=[i for i in cand if i!=[]]
if ans==[]:
  print('UNRESTORABLE')
else:
  ans.sort()
  print(*ans[0],sep='')
