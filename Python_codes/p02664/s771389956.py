s=list(input())
for i in range(len(s)):
  if s[i]=='?':
    s[i]='D'
print(''.join(map(str,s)))