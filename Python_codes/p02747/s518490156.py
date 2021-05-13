s=input()

ans='Yes'

if len(s)%2==0:
  for i in range(len(s)):
    if i%2==0:
      if s[i]=='h':
        ans='Yes'
      else:
        ans='No'
        break
    else:
      if s[i]=='i':
        ans='Yes'
      else:
        ans='No'
        break
else:
  ans='No'

print(ans)