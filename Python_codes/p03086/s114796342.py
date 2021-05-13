S=input()
bit=[0]*len(S)
for i in range(len(S)):
  if S[i]=="A" or S[i]=="T" or S[i]=="G" or S[i]=="C":
    bit[i]=1
count=[0]*len(S)
for i in range(len(S)):
  if bit[i]==0 :
    continue
  else :
    count[i]+=1
    for j in range(i+1,len(S)):
      if bit[j]==1 :
        count[i]+=1
      else :
        break
print(max(count))