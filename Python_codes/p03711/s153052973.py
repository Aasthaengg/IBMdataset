x,y=map(int,input().split())
a=[1,3,5,7,8,10,12]
count=0
if x in a:
    if y in a:
        count+=1
    else:
        count+=0
if x not in a and x!=2:
    if y not in a and y!=2:
        count+=1
    else:
        count+=0
if x==2:
    if y==2:
        count+=1
    else:
        count+=0
if count!=0:
    print('Yes')
else:
    print('No')