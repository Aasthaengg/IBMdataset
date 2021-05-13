N=int(input())
S=input()
hw=[]
i=0
while i<N:
  if i+1<N and S[i]==S[i+1]:
    hw.append(2)
    i+=2
  else:
    hw.append(1)
    i+=1
mod=10**9+7
ans=0
for i in range(len(hw)):
  if i==0:
    if hw[i]==1:
      ans=3
    else:
      ans=6
  if i!=0:
    if hw[i]==1 and hw[i-1]==1:
      ans*=2
      ans%=mod
    if hw[i]==1 and hw[i-1]==2:
      ans*=1
    if hw[i]==2 and hw[i-1]==1:
      ans*=2
      ans%=mod
    if hw[i]==2 and hw[i-1]==2:
      ans*=3
      ans%=mod

print(ans)      