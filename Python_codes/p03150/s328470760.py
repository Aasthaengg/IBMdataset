s1="keyence"
s=input()
k=-1
for i in range(len(s)):
    if s[i]!=s1[i]:
        k=i
        break
if k==-1:
    print("YES")
else:
    if s[:k]+s[len(s)-7+k:]==s1:
        print("YES")
    else:
        print("NO")