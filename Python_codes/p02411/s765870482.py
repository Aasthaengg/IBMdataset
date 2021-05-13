a,b,c=map(int,input().split())
while a!=-1 or b!=-1 or c!=-1:
    if a==-1 or b==-1:
        print('F')
    else:
        if a+b>=80:
            print('A')
        elif 80>a+b>=65:
            print('B')
        elif 65>a+b>=50:
            print('C')
        elif 50>a+b>=30:
            if c>=50:
                print('C')
            else:
                print('D')
        else:
            print('F')
    a,b,c=map(int,input().split())
