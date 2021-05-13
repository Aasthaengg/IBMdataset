s=input().replace("BC","D")
s=s+"0"
count=0
ans=0
for i in range(len(s)):
    if s[i]=="A":
        count+=1
    elif s[i]=="D":
        ans+=count
    else:
        count=0
print(ans)