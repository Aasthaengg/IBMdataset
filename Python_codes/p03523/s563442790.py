# A - AKIBA
S = str(input())

# 文字列からAを抜いて KIHBRになればOK

if S.find('AA') == -1 :
    if S.find('KA') == -1 :
        if S.find('IA') == -1:
            S2 = S.replace('A','')
            if S2 == 'KIHBR':
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
    else:
        print('NO')
else:
    print('NO')