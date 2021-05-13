S=input()
count=0
s=list(S)
for i in range(len(S)):
    if (i+1)%2!=0:
        if s[i]=='R' or s[i]=='U' or s[i]=='D':
            count+=1
    else:
        if s[i]=='L' or s[i]=='U' or s[i]=='D':
            count+=1
if count==len(S):
    print('Yes')
else:
    print('No')