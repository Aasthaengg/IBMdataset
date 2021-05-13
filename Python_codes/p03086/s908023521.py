s=input()
ans=0
c=0
for i in range(len(s)):
    if s[i] in ["A","C","G","T"]:
        c+=1
    else:
        c=0
    ans=max(ans,c)
print(ans)