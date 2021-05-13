s=input()
l=0
r=len(s)-1
cnt=0
while(l<r):
    if s[l]==s[r]:
        l+=1
        r-=1
    elif s[l]=="x":
        cnt+=1
        l+=1
    elif s[r]=="x":
        cnt+=1
        r-=1
    else:
        cnt=-1
        break
print(cnt)