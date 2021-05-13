l=list(map(int,input().split()))
x,y=l[0]+l[1],l[2]+l[3]
if(x>y):
    print("Left")
elif(x==y):
    print("Balanced")
else:
    print('Right')