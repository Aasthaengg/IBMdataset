x,y=map(int,input().split())
p=0
for i in range (1,x+1):
    if i*2+(x-i)*4==y or i*4+(x-i)*2==y:
        p=1
if p==1:
    print("Yes")
else:
    print("No")