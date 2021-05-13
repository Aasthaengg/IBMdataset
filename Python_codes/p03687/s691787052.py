s=input()
str1=set()
ans=len(s)
for i in range(len(s)):
    str1.add(s[i])
for i in range(len(str1)):
    str2=str1.pop()
    sans=0
    if s[0]==str2:
        cnt=0
    else:
        cnt=1
    for j in range(1,len(s)):
        if s[j]!=str2:
            cnt+=1
        else:
            sans=max(sans,cnt)
            cnt=0
    sans=max(sans,cnt)
    ans=min(ans,sans)
print(ans)
