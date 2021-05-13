s = input()
isC = s.find('C')
ret = False
if(  isC != -1):
    if( s[isC+1:].find('F') != -1):
        ret = True
if ret:
    print('Yes')
else:
    print('No')