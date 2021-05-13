S = input()
mod=10**9+7

suma,sumc,sumq=0,0,0
maxC=S.count("C")%mod
maxQ=S.count("?")%mod
ans1,ans2,ans3,ans4=0,0,0,0

for i,s in enumerate(S):
  if s=="A":
    suma+=1
    suma%=mod
  elif s=="C":
    sumc+=1
    sumc%=mod
  elif s=="?":
    sumq+=1
    sumq%=mod
  
  if i==0 or i==len(S):
    continue
  
  if s=="?":
    ans2+=suma    *(maxC-sumc)%mod
    ans3+=(sumq-1)*(maxC-sumc)%mod
    ans3+=suma    *(maxQ-sumq)%mod
    ans4+=(sumq-1)*(maxQ-sumq)%mod
  elif s=="B":
    ans1+=suma*(maxC-sumc)%mod
    ans2+=sumq*(maxC-sumc)%mod
    ans2+=suma*(maxQ-sumq)%mod
    ans3+=sumq*(maxQ-sumq)%mod
    
ans1*=3**maxQ%mod
ans2*=3**(maxQ-1)%mod
ans3*=3**(maxQ-2)%mod
ans4*=3**(maxQ-3)%mod
ans=ans1+ans2+ans3+ans4
print(int(ans%mod))