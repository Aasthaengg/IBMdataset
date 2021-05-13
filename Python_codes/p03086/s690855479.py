s=input()
ans=0
for i in range(len(s)):
    for j in range(len(s)):
        new_s=list(s[i:(len(s)-j)])
        if all((i in ["A","T","G","C"]) for i in new_s) and len(new_s)>ans:
            ans=len(new_s)
print(ans)