S=input()
T=input()
t=len(T)
s=len(S)
if s<t:
  print("UNRESTORABLE")
  exit()
L=list()
for i in range(s-t+1):
  "S[i]からs[i+t-1]までの文字列"
  for j in range(t):
    if S[i+j]!="?" and S[i+j]!=T[j]:
      break
    if j==t-1:
      k=S[:i]+T+S[i+t:]
      k=k.replace("?","a")
      L.append(k)
if len(L)==0:
  print("UNRESTORABLE")
else:
  L=sorted(L)
  print(L[0])