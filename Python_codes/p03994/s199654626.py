s=list(input())
k=int(input())
for i in range(len(s)):
    if i==len(s)-1:
        s[-1]=chr((ord(s[i])-97+k)%26+97)
        break
    if s[i]=='a':
        continue
    if 123-ord(s[i])<=k:
        k-=123-ord(s[i])
        s[i]='a'
print(*s,sep='')