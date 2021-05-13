n=int(input())
s1=input()
s1_=list(s1)
s2=input()
for i in range(len(s1)-1):
  if s1[i]==s1[i+1]:
    idx=s1_.index(s1[i])
    s1_[idx+1]='1'
    del s1_[idx]
mod=10**9+7
if s1_[0]=='1':
  ans=6
else:
  ans=3
#print(s1_)
for i in range(1,len(s1_)):
  if s1_[i]=='1':
    if s1_[i-1]!='1':
      ans*=2
      ans%=mod
    else:
      ans*=3
      ans%=mod
  else:
    if s1_[i-1]!='1':
      ans*=2
      ans%=mod
print(ans%mod)