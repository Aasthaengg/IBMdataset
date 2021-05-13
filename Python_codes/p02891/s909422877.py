s=input()
n=len(s)
k=int(input())
if k==1:
  if n==1:
    print(0)
  else:
    i=1
    cnt=0
    while i<n:
      if s[i-1]==s[i]:
        cnt+=1
        i+=1
      i+=1
    print(cnt)
else:
  single=True
  for c in s:
    if c!=s[0]:
      single=False
      break
  if single:
    print(n*k//2)
  elif s[0]!=s[-1]:
    i=1
    cnt=0
    while i<n:
      if s[i-1]==s[i]:
        cnt+=1
        i+=1
      i+=1
    print(cnt*k)
  else:
    i=1
    while s[i]==s[0]:
      i+=1
    kk=i
    j=-1
    while s[j]==s[0]:
      j-=1
    num=i-j-1
    cnt=0
    i+=1
    while i<=n+j:
      if s[i-1]==s[i]:
        cnt+=1
        i+=1
      i+=1
    print(cnt*k+num//2*(k-1)+kk//2+(-j-1)//2)
