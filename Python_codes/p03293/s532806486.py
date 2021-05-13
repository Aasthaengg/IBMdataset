S = str(input())
T = str(input())

flg = False
ok = False


if S == T:
    print('Yes')
else:
    for i in range(0,len(S)-1):
        temp = S[-i-1:]
        ret = temp + S[:len(S)- i -1]
        
        if ret == T:
            flg = True
            break
        
    if flg == True:
        print('Yes')
    else:
        print('No')