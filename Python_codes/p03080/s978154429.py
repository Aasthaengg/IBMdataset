N=int(input())
s=list(input())
R=0
B=0
for i in range(len(s)):
    if s[i]=='R':
        R+=1
    if s[i]=='B':
        B+=1
if R>B:
    print('Yes')
else:
    print('No')