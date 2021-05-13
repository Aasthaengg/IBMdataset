a,b = map(int, input().split())

if a ==1:
    if b == 1:
        print(1)
        exit()
    else:
        print(b-2)
        exit()

elif a==2:
    print(0)
    exit()

else:
    if b ==1:
        print(a-2)
        exit()
    elif b==2:
        print(0)
        exit()
    else:
        print((a-2)*(b-2))
        exit()