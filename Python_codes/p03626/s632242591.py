n=int(input())
s1=list(input())
s2=list(input())
x=-1
if s1[0]==s2[0]:
  ct=3;k=1;p=1
else:
  ct=6;k=2;p=2
for i in range(k,n):
  if x!=i:
    if s1[i]==s2[i]:
      if p==1:
        ct*=2;p=1
      else:
        ct*=1;p=1
    else:
      x=i+1
      if p==1:
        ct*=2;p=2
      else:
        ct*=3;p=2
    ct%=(10**9+7)
print(ct)