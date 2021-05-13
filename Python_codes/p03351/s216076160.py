a,b,c,d=map(int,input().split())
if (a-c)**2 <= d*d:
    print("Yes")
else:
    if (a-b)**2 > d*d:
        print("No")
    elif (b-c)**2 >d*d:
        print("No")
    else:
        print("Yes")