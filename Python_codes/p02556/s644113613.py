N=int(input())
minz=10**11
minw=10**11
maxz=-10**11
maxw=-10**11
for i in range(N):
 
    a,b=map(int,input().split())
    if  a+b>maxz:
        maxz=a+b

    if a+b<minz:
        minz=a+b

    if  a-b>maxw:
        maxw=a-b

    if a-b<minw:
        minw=a-b

    
 
print(max((maxz-minz),(maxw-minw)))