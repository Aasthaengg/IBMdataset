import sys
lst = [input() for i in range(3)]
#print(lst)
init = lst[0][0]
while True:
    if init == 'a':
        if len(lst[0]) == 0:
            print('A')
            sys.exit()
        else:
            init = lst[0][0]
            lst[0]=lst[0][1:]
        
    elif init =='b':
        if len(lst[1]) == 0:
            print('B')
            sys.exit()
        else:
            init = lst[1][0]
            lst[1]=lst[1][1:]
        
    else:
        if len(lst[2]) == 0:
            print('C')
            sys.exit()
        else:
            init = lst[2][0]
            lst[2]=lst[2][1:]
    
    #print(lst)