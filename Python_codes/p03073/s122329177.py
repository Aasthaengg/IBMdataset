s=input()
cnt=0
ans=0
for i in range(len(s)):
  if i%2==0:
    if s[i]=='0':
      cnt+=1
  else:
    if s[i]=='1':
      cnt+=1
for i in range(len(s)):
  if i%2==0:
    if s[i]=='1':
      ans+=1
  else:
    if s[i]=='0':
      ans+=1
print(min(cnt,ans))