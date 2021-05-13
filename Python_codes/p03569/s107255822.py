s=input()
temp=""
for c in s:
     if c!="x": temp+=c
if temp!=temp[::-1]: print(-1)
elif len(temp)==0:  print(0)
else:
    a=temp[0:len(temp)//2]
    l,r=0,len(s)-1
    ans=0
    while l<r:
        if s[l]==s[r]:
            l+=1
            r-=1
            continue
        elif s[l]=="x": l+=1
        else: r-=1
        ans+=1
    print(ans)