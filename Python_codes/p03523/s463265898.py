s=input()
t=''
for i in range(len(s)):
    if s[i]!='A':
        t+=s[i]
ans=''
if t=='KIHBR':
    cnt=0
    if s[s.index('K')+1]=='I' and s[s.index('I')+1]=='H':
        for i in range(len(s)):
            if s[i]=='A':
                cnt+=1
                if cnt==2:
                    ans='NO'
                    break
            else:
                cnt=0
        if cnt<2:
            ans='YES'
        else:
            ans='NO'
    else:
        ans='NO'
else:
    ans='NO'
print(ans)