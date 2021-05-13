x,y=map(int,input().split())
if ((x in [1,3,5,7,8,10,12])&(y in [1,3,5,7,8,10,12]))|((x in [4,6,9,11])&(y in [4,6,9,11]))|((x==2)&(y==2)):
    print("Yes")
else:
    print("No")