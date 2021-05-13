x=[1,3,5,7,8,10,12]
y=[4,6,9,11]
z=[2]
l,r=map(int,input().split())
if(l in x and r in x):
    print("Yes")
elif(l in y and r in y):
    print("Yes")
elif(l in z and r in z):
    print("Yes")
else:
    print("No")