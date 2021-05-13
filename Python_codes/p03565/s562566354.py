S=input()
T=input()
l_s=len(S)
l_t=len(T)
ans=[]
i=0
while i+l_t<=l_s:
  j=0
  while j<l_t:
    if S[i+j]=="?" or S[i+j]==T[j]:
      j+=1
    else:
      break
  if j==l_t:
    A=S[:i]+T+S[i+l_t:]
    A=A.replace("?","a")
    ans.append(A)
  i+=1
print(sorted(ans)[0] if ans else "UNRESTORABLE")
