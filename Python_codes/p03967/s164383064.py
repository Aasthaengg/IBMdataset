s=input()
c=0
ans=0
for i in range(len(s)):
    if s[i]=="g":
        c+=1
    else:
        if c>0:
            c-=1
        else:
            ans-=1
ans+=c//2
print(ans)
