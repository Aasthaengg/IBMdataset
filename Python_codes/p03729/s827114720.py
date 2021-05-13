a,b,c = map(str,input().split())
isOK = False
if a[-1]==b[0] and b[-1]==c[0]:
    isOK = True

if isOK:
    print('YES')
else:
    print('NO')