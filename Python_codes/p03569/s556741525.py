s=list(input())
ans=0
for i in range(len(s)):
    if len(s)<=1:
        break
    if s[0]==s[-1]:
        del s[0]
        del s[-1]
    else:
        if s[0]=="x":
            ans+=1
            del s[0]
        elif s[-1]=="x":
            ans+=1
            del s[-1]
        else:
            ans=-1
            break
print(ans)
