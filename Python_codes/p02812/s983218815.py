N=int(input())
S=input()
 
slen=len(S)
nabc=0
for i in range(0,slen-2):
  if S[i:i+3]=='ABC':
    nabc+=1
 
print(nabc)