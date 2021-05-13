s=input()
res=[0]*26
for i in range(len(s)):
    res[ord(s[i])-97]=1
ans="-1"
for i in range(26):
    if res[i]==0:
        ans=s+chr(i+97)
        break
if ans=="-1":
    for i in range(26):
        for j in range(ord(s[25-i])-96,26):
            if res[j]==0:
                ans=s[:25-i]+chr(j+97)
                break
        if ans!="-1":
            break
        res[ord(s[25-i])-97]=0
print(ans)