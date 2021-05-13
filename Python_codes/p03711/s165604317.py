x,y=input().split()
x=int(x);
y=int(y);
l1=[1,3,5,7,8,10,12]
l2=[4,6,9,11]
if(x in l1 and y in l1):
    print("Yes")
elif(x in l2 and y in l2):
    print("Yes")
elif(x==2 and y==2):
    print("Yes")
else:
    print("No")