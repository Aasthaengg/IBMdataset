s=input()
a=s.replace('x','')
for i in range(len(a)):
    if a[i]!=a[-1-i]:
        print(-1)
        exit()
l=0
r=len(s)-1
ans=0
while l<r:
    if s[l]==s[r]:
        l+=1
        r-=1
    elif s[l]=='x':
        l+=1
        ans+=1
    elif s[r]=='x':
        r-=1
        ans+=1
print(ans)