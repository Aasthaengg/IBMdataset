while True:
    a,b,c = map(int,input().split())
    if a == b == c == -1: break
    if a==-1 or b==-1:
        print('F')
        continue
    if 80 <= a+b:
        print('A')
        continue
    elif 65 <= a+b:
        print('B')
        continue
    elif 50 <= a+b:
        print('C')
        continue
    elif 30 <= a+b:
        if 50 <= c:
            print('C')
            continue
        else:
            print('D')
            continue
    elif a+b<30: print('F')
    

