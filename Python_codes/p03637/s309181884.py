n=int(input())
a=list(map(int,input().split()))
x=0 #odd
y=0 #2
z=0 #4
for i in a:
    if i%4==0:
        z+=1
    elif i%2==0:
        y+=1
    else:
        x+=1
if x<=z:
    print("Yes")
else:
    if x==z+1 and y==0:
        print("Yes")
    else:
        print("No")
