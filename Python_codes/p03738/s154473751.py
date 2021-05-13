a = input()
b = input()

if len(a) != len(b):
    print('GREATER' if len(a) > len(b) else 'LESS' if len(a) < len(b) else 'EQUAL')
else:
    flg  = True
    for k,v in zip(a,b):
        if k > v:
            flg = False
            print('GREATER')
            break
        elif k < v:
            flg = False
            print('LESS')
            break
        else:
            pass
        
    if flg:
        print('EQUAL')