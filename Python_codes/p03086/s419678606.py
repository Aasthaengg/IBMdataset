s = input()
mx=0
cnt=0
for i in range(len(s)):
    if s[i]=='A'or s[i]=='C'or s[i]=='G'or s[i]=='T':
        cnt+=1
    else:
        mx=max(mx,cnt)
        cnt=0
mx=max(mx,cnt)
print(mx)
