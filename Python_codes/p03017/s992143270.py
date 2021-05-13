n,a,b,c,d=map(int,input().split())
s=input()
if c<d and b<c:
  s=s[a-1:d]
elif c>d and b<c:
  t=s[b-2:d+1]
  s_=s[a-1:c]
elif a<c<b<d:
  s_=s[a-1:c]
  s=s[b-1:d]
  f=0
  f_=0
  for i in range(len(s_)):
    if s_[i]=='.':
      f=0
    elif s_[i]=='#' and f==0:
      f=1
    elif s_[i]=='#' and f==1:
      print('No')
      exit()
  for j in range(len(s)):
    if s[i]=='.':
      f_=0
    elif s[i]=='#' and f_==0:
      f_=1
    elif s[i]=='#' and f_==1:
      print('No')
      exit()
  print('Yes')
  exit()
if c<d:
  f=0
  for i in range(len(s)):
    if s[i]=='.':
      f=0
    elif s[i]=='#' and f==0:
      f=1
    elif s[i]=='#' and f==1:
      print('No')
      exit()
  print('Yes')
else:
  f=0
  g=0
  h='No'
  for i in range(len(s_)):
    if s_[i]=='.':
      f=0
    elif s_[i]=='#' and f==0:
      f=1
    elif s_[i]=='#' and f==1:
      print('No')
      exit()
  for j in range(len(t)):
    if t[j]=='.':
      g+=1
      if g==3:
        h='Yes'
    else:
      g=0
  print(h)    
