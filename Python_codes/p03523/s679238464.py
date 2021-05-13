s = input()

conList = []
for i in range(16):
    flag = str(bin(i))[2:].zfill(4)
    a = ''
    if( flag[0] == '1'):
        a = a+'A'
    a = a+'KIH'
    if( flag[1] == '1'):
        a = a+'A'   
    a = a+'B'
    if( flag[2] == '1'):
        a = a+'A'  
    a = a+'R'
    if( flag[3] == '1'):
        a = a+'A' 
    conList.append(a) 
if( s in conList):
    print('YES')
else:
    print('NO')