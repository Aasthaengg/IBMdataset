s=input()
count=0
ans=0
for i in range(len(s)):
    if s[i]=="B":
        count+=1
    elif s[i]=="W":
        ans+=count
print(ans)