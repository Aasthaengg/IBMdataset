s=input()
d=s.replace("x","")
rd=d[::-1]
if d!=rd:print(-1)
else:
    ans=0
    x,y=0,len(s)-1
    while y-x>0:
        if s[x]==s[y]:
            x+=1;y-=1
        elif s[x]=="x":
            ans+=1;x+=1
        else:
            ans+=1;y-=1
    print(ans)