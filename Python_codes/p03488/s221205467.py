s=input()
x,y=list(map(int,input().split()))
dx=[]
dy=[]
first=True
move=0
xf=0
dir=0
for i in s:
    if(i=="F"):
        move+=1
    else:
        if(first):
            xf = move
            first=False
        else:
            if(dir%2==0):
                dx.append(move)
            else:
                dy.append(move)
        dir+=1
        move=0

if(dir%2==0):
    if(first):
        xf = move
    else:
        dx.append(move)
else:
    dy.append(move)
cx=0
cy=0
x-=xf
for i in sorted(dx,reverse=True):
    if x>=cx:
        cx+=i
    else:
        cx-=i

for i in sorted(dy,reverse=True):
    if y>=cy:
        cy+=i
    else:
        cy-=i
#print(sorted(dx,reverse=True),sorted(dy,reverse=True))
if(cx==x and cy==y):
    print("Yes")
else:
    print('No')
