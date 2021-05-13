s=input()
t=input()
ans=[]
for i in range(len(s)-len(t)+1):
  for j in range(len(t)):
    if s[i+j]!=t[j] and s[i+j]!='?':break
  else:
    a=''
    for k in s[0:i]+t+s[i+len(t):]:
      if k=='?':a+='a'
      else:a+=k
    ans+=[a]
ans=sorted(ans)
if ans:print(ans[0])
else:print('UNRESTORABLE')