s=input()
total=0
ans=0
for i in range(len(s)):
    if s[i]=="W":
        total+=i-ans
        ans+=1
print(total)