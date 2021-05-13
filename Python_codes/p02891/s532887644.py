S=input()
K=int(input())
N=len(S)
count=1
countlist=[]
anssub=0
for i in range(N-1):
  if S[i]==S[i+1]:
    count+=1
  else: 
    countlist+=[count]
    count=1
if S[N-2]!=S[N-1]:
  count=1
countlist+=[count]  
for i in range(len(countlist)):
  if i!=0 and i!=len(countlist)-1:
    if countlist[i]!=1:
      anssub+=countlist[i]//2
a=countlist[0]+countlist[-1]
if S[0]==S[-1]:
  anssub2=a//2
else:
  anssub2=0
  if countlist[0]!=1:
    anssub2+=countlist[0]//2
  if countlist[-1]!=1:
    anssub2+=countlist[-1]//2
  
b=countlist[0]
c=countlist[-1]
anssub3=0
if b!=1:
  anssub3+=b//2
if c!=1:
  anssub3+=c//2
  
ans=anssub*K+anssub2*(K-1)+anssub3
if len(countlist)==1:
  ans=countlist[0]*K//2
print(ans)