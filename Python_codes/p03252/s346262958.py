from collections import defaultdict
d = defaultdict(int)
ans=0
S=input()
T=input()
for i in range(len(S)):
 if d[S[i]]==0 or d[S[i]]==T[i]:
  d[S[i]]=T[i]
 else:
  ans+=1
  break
d = defaultdict(int)
for i in range(len(S)):
 if d[T[i]]==0 or d[T[i]]==S[i]:
  d[T[i]]=S[i]
 else:
  ans+=1
  break
if ans>0:
 print("No")
else:
 print("Yes")