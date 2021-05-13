x,y,z,d=map(int,input().split())
if((abs(y-x)<=d and abs(z-y)<=d) or abs(z-x)<=d):
    print("Yes")
else:
    print("No")
