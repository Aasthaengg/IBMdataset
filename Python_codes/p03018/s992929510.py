s=input()

while 'BC' in s:
    s=s.replace('BC','D')
ans=0
a=0
for i in range (len(s)):
    if s[i]!='A' and s[i]!='D':
        a=0
        continue
    elif s[i]=='A':
        a+=1
    elif s[i]=='D':
        ans+=a
print(ans)