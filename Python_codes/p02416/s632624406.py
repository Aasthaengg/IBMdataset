while(True):
    a = input()
    if(a == '0'):
        break
    b = [int(i) for i in list(str(a))]
    print(sum(b))