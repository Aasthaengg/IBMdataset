s=input()
str1=s[0]
str2=""
ans=1
for i in range(len(str1),len(s)):
    str2+=s[i]
    if str1!=str2:
        ans+=1
        str1=str2
        str2=""
print(ans)
