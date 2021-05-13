n=int(input())
lp=[]
lm=[]
for i in range(n):
    s=input()
    x,y=0,0
    for j in s:
        if j=="(":
            x+=1
        else:
            x-=1
        y=min(y,x)
    if x>0:
        lp.append((y,x))
    else:
        lm.append((y-x,-x))
lp.sort()
s=0
for i,j in lp[::-1]:
    if s+i<0:
        print("No")
        exit()
    s+=j
lm.sort()
t=0
for i,j in lm[::-1]:
    if t+i<0:
        print("No")
        exit()
    t+=j
if s==t:
    print("Yes")
else:
    print("No")