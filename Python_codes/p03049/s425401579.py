_,*s=open(0).read().split()
a=b=c=d=0
for S in s:
 c+=S.count('AB')
 if S[-1]=='A':
  a+=1
  if S[0]!='B':d=1
 if S[0]=='B':
  b+=1
  if S[-1]!='A':d=1
print(c+max(min(a,b)+d-1,0))
