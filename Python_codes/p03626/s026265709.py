MOD=10**9+7
N=int(input())
S1=input()
S2=input()

if N==1:
  print(3)
  exit()

if S1[0]==S2[0]:
  ans,i=3,1
else:
  ans,i=6,2

while i<N:
  if S1[i]==S2[i]:
    if S1[i-1]==S2[i-1]:
      ans=ans*2%MOD
    i+=1
  else:
    if S1[i-1]==S2[i-1]:
      ans=ans*2%MOD
    else:
      ans=ans*3%MOD
    i+=2
    
print(ans)