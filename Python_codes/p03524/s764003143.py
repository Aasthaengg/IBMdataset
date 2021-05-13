s=input()
cnt=[0]*3
ans="YES"
for i in range(len(s)):
    cnt[ord(s[i])-97]+=1
if max(cnt)-min(cnt)>=2:
    ans="NO"
print(ans)