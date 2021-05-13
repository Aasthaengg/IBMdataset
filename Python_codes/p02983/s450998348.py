l,r=map(int,input().split())
s=10000
for i in range(l,r+1):
    if i%2019==0:
        s=0
        break
    elif (i%673==0 and r-l!=1) or (i%673==0 and (r%3==0 or l%3==0)):
        s=0
        break
if s==0:
    print(0)
else:
    t=10000
    for i in range(l,r):
        for j in range(i+1,r+1):
            if ((i%2019)*(j%2019))%2019<t:
                t=((i%2019)*(j%2019))%2019
    print(t)