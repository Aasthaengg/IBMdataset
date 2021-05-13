x,y=map(int,input().split())
a=[1,3,5,7,8,10,12]
b=[4,6,9,11]
if a.count(x)==1 and a.count(y)==1:
    print("Yes")
elif b.count(x)==1 and b.count(y)==1:
    print("Yes")
else:
    print("No")
