argStr = input()
ret=0
tmp=0
flag = False
for s in argStr:
    
    if (s=='A') | (s == 'C') | (s=='G') | (s=='T'):
        flag = True
        tmp+=1
    else:
        if flag :
            if( ret < tmp):
                ret = tmp
                tmp = 0
            flag = False
if( ret < tmp):
    ret = tmp
print(ret)
