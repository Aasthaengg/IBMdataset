S=list(input())

nS=[]
i=0
while i<len(S)-1:
  if S[i]=="B" and S[i+1]=="C":
    nS.append("D")
    i+=1
  else:
    nS.append(S[i])
  i+=1
    
t=[]
nl=[]
for i in nS:
  if i=="A" or i=="D":
    nl.append(i)
  else:
    if nl:
      t.append(nl)
      nl=[]
if nl:
  t.append(nl)


ans=0
for i in t:
  dn=0
  for j in range(len(i)):
    if i[j]=="D":
      ans+=j-dn
      dn+=1

print(ans)
