x,y=2,1
n=int(input())
if(n==1):
    print(1)
elif(n==0):
    print(0)
else:
    for i in range(n-1):
        z=x+y
        x=y
        y=z
    print(z)
