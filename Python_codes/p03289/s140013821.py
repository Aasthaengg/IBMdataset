s=input()
ans="AC"
if s[0]!='A' or s[-1]=='C' or s[1]<'a':ans="WA"
else:
    count=0
    for i in range(2,len(s)):
        if s[i]<'a':
            if s[i]=='C':count+=1
            else:count+=2
    if count!=1:ans="WA"
print(ans)
