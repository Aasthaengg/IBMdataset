S=input()
count=0
for i in range(2,len(S)-1):
  if S[i]=="C" :
    iC=i
    count+=1
temp=[]
if S[0]=="A" and count==1 :
  for i in range(len(S)):
    if i!=0 and i!=iC :
      temp.append(S[i])
  if (''.join(temp)).islower()==True :
    print("AC")
    exit()
print("WA")