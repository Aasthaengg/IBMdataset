x,y=input().split()
x=int(x)
y=int(y)
if x==2 | y==2:
    print('No')
    exit()
lt1=[1,3,5,7,8,10,12]
lt2=[4,6,9,11]
if (lt1.count(x)==1 and lt1.count(y)==1) or (lt2.count(x)==1 and lt2.count(y)==1):
    print('Yes')
else:
    print('No')