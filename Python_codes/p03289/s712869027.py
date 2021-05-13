s = str(input())
moji = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
isOK = True
if s[0]=='A':
    tmp = s[2:-1]
    cnt = 0
    for i in range(len(tmp)):
        if tmp[i]=='C':
            cnt += 1
    if cnt!=1:
        isOK = False
else:
    isOK = False

cnt = 2
for i in range(len(s)):
    if s[i] in moji:
        cnt += 1
if len(s)!=cnt:
    isOK = False

if isOK:
    print('AC')
else:
    print('WA')