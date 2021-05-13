s=input()
ans=0
c=1#連続数
temp=0
for i in range(len(s)):
    if i==0:
        ans+=1
    else:
        if s[i]==">" and s[i]==s[i-1]:
            c+=1
            if temp>=c:
                ans+=c-1
            else:
                ans+=c
        elif s[i]==">" and s[i]!=s[i-1]:
            temp=c
            c=1
        elif s[i]=="<" and s[i]==s[i-1]:
            c+=1
            ans+=c
        elif s[i]=="<" and s[i]!=s[i-1]:
            c=1
            tmp=0
            ans+=1
    #print(ans)
print(ans)