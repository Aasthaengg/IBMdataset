s = str(input())
isError = False
for i in range(len(s)):
    if i%2==0:
        if s[i]=='L':
            isError = True
    else:
        if s[i]=='R':
            isError = True
if isError:
    print('No')
else:
    print('Yes')
