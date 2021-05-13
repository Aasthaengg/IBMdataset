x,y = map(int,input().split())
dum1 = [1,3,5,7,8,10,12]
dum2 = [4,6,9,11]
if x == 2:
    print("No")
else:
    if dum1.count(x) == 1 and dum1.count(y) == 1:
        print("Yes")
    elif dum2.count(x) == 1 and dum2.count(y) == 1:
        print("Yes")
    else:
        print("No")