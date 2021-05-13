S=input()
S=S[::-1]
ans=0
count=0
for i in range(len(S)):
  if(S[i]=="W"):
    count+=1
  elif(S[i]=="B"):
    ans+=count
print(ans)