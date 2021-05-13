s=input()
maxx=0
tmp=0
for i in range(len(s)):
    if s[i]== 'A' or s[i]=='T' or s[i]=='G' or s[i]=='C':
        tmp+=1
        maxx=max(maxx,tmp)
    else:
        tmp=0
print(maxx)