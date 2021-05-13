s=list(input())
ans=0
for i in range(len(s)):
    if s[i]=='C':
        ans+=1
        break
for j in range(i,len(s)):
    if s[j]=='F':
        ans+=1
        break
if ans==2:
    print('Yes')
else:
    print('No')
