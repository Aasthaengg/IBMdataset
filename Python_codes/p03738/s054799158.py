a=input()
b=input()
if(len(a)>len(b)):
    print('GREATER')
elif(len(b)>len(a)):
    print('LESS')
else:
    fla,flb=0,0
    for i in range(len(a)):
        if(int(a[i])>int(b[i])):
            fla=1
            break
        if(int(b[i])>int(a[i])):
            flb=1
            break
    if(fla==0 and flb==0):
        print('EQUAL')
    elif(fla==1):
        print('GREATER')
    else:
        print('LESS')
        
