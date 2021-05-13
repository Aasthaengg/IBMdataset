s=list(input())
o=0
z=len(s)
for i in range(len(s)):
    if s[i]=='o':
        o+=1
if o+(15-z)>=8:
    print('YES')
else:
    print('NO')
