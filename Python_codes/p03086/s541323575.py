s=input()
count=0
ans=0
for i in range(len(s)):
    if s[i]=="A" or s[i]=="G" or s[i]=="C" or s[i]=="T":
        count+=1
    else:
        ans=max(ans,count)
        count=0
print(max(ans,count))