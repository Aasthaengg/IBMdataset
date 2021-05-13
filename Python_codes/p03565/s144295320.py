s=list(input())
t=list(input())
ans='U'
for i in range(len(s)-len(t),-1,-1):
  if s[i]==t[0] or s[i]=='?':
    cnt=1
    for j in range(1,len(t)):
      if s[i+j]==t[j] or s[i+j]=='?':
        cnt+=1
    if cnt==len(t):
      s[i:i+len(t)]=t
      u=''
      for k in s:
        u+=k
      u=u.replace('?','a')
      print(u)
      exit()
      
print('UNRESTORABLE')
